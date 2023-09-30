from abc import abstractmethod
from ..animal import Animal

class Bird(Animal):
    def __init__(self, name, height, weight, colorEye, fly):
        self.fly = fly
        super().__init__(name, height, weight, colorEye)