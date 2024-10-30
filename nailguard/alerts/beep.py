from pathlib import Path
from time import sleep

import pygame

from .base import Alert


class BeepAlert(Alert):
    
    def __init__(self):
        pygame.mixer.init()
        sound_path = str(Path(__file__).parent.parent / "assets" / "error.wav")
        self.sound = pygame.mixer.Sound(sound_path)
    
    def fire(self):
        self.sound.play()
        sleep(1.0)
