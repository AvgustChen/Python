from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, height, weight, color_eye):
        self.name = name
        self.height = height
        self.weight = weight
        self.color_eye = color_eye

    def __str__(self) -> str:
        return f"{self.name}; Рост: {self.height}; Вес: {self.weight}; Цвет глаз: {self.color_eye};"

    @abstractmethod
    def animalSay(self):
        return (f"{self.name} сказал(а): ")
