from ..intarfaces.dogTraining import DogTraining
from .home import Home


class Dog(Home, DogTraining):

    def __init__(self, name, height, weight, color_eye, name2, breed, vaccination, color, date, wool):
        self.wool = wool
        super(Dog, self).__init__(name, height, weight, color_eye, name2, breed, vaccination, color, date)

    def animalSay(self):
        print(f"{super().animalSay()} 'Гав-гав'")

    def caressing(self):
        return (super().caressing())

    def training(self):
        DogTraining.training(self)

    def __str__(self) -> str:
        return (f"{super().__str__()} Наличие шерсти: {self.wool};")