from .home import Home


class Cat(Home):
    def __init__(self, name, height, weight, color_eye, name2, breed, vaccination, color, date, wool):
        self.wool = wool
        super(Cat, self).__init__(name, height, weight, color_eye, name2, breed, vaccination, color, date)

    def animalSay(self):
        print(f"{super().animalSay()} 'Мяу'")

    def caressing(self):
        return (super().caressing())

    def __str__(self) -> str:
        return (f"{super().__str__()} Наличие шерсти: {self.wool};")