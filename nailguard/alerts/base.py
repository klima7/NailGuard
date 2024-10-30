from abc import ABC, abstractmethod


class Alert(ABC):
    
    @abstractmethod
    def fire(self):
        pass
