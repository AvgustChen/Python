from abc import abstractmethod
from ..animal import Animal


class Home(Animal):
    def __init__(self, name, height, weight, color_eye, name2, breed, vaccination, color, date):
        self.name2 = name2
        self.breed = breed
        self.vaccination = vaccination
        self.color = color
        self.date = date
        super(Home, self).__init__(name, height, weight, color_eye)

    @abstractmethod
    def caressing(self):
        print(f"{self.name} {self.name2} хочет ласки!!!")

    def __str__(self) -> str:
        return (f"{super().__str__()} Кличка: {self.name2}; Порода: {self.breed}; "
                f"Наличие прививки: {self.vaccination}; Цвет: {self.color}; Дата рождения: {self.date};")
