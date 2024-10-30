from pathlib import Path
from time import sleep

from beepy import beep

from .base import Alert


class BeepAlert(Alert):
    
    def __init__(self):
        self.icon_path = str(Path(__file__).parent.parent / "assets" / "stop.png")
    
    def fire(self):
        beep(3)
        sleep(0.5)
