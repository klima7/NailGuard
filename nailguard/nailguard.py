import threading

import cv2
from PIL import Image
from nailguard.detectors import Detector
from nailguard.alerts import Alert


class Nailguard:
    
    def __init__(
        self,
        detectors: list[Detector],
        alerts: list[Alert],
        camera_idx: int,
        trigger_count: int,
        debounce: float
    ) -> None:
        self.detectors = detectors
        self.alerts = alerts
        self.camera_idx = camera_idx
        self.trigger_count = trigger_count
        self.debounce = debounce
        
        self.image = None
        self.detected = {detector: False for detector in detectors}
    
    def run(self) -> None:
        threading.Thread(target=self._image_thread, args=(self,)).start()
        
        for detector in self.detectors:
            threading.Thread(target=self._detector_thread, args=(self, detector)).start()

    @staticmethod
    def _image_thread(nailguard) -> None:
        cap = cv2.VideoCapture(nailguard.camera_idx)
        while True:
            ret, image = cap.read()
            if not ret:
                raise Exception("Failed to capture image from camera")
            
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            nailguard.image = image
        
    @staticmethod
    def _detector_thread(nailguard, detector: Detector) -> None:
        while True:
            if nailguard.image is None:
                continue
            
            bite = detector.detect(nailguard.image)
            nailguard.detected[detector] = bite
            print(bite)
