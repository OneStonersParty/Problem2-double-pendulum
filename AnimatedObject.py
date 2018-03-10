from abc import ABC, abstractmethod

class AnimatedObject(ABC):
    @abstractmethod
    def __init__(self,ax):
        pass
    def simulate(self, deltaT): # simulate forward a time of deltaT
        pass
    def drawing(self): # return current picture
        pass
