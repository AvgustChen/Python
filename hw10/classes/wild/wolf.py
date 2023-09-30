from .wild import Wild


class Wolf(Wild):
    def __init__(self, name, height, weight, color_eye, place, date, leader):
        self.leader = leader
        super(Wolf, self).__init__(name, height, weight, color_eye, place, date)

    def animalSay(self):
        print(f"{super().animalSay()} уууУУУ")

    def __str__(self) -> str:
        if (self.leader == True):
            return f"{super().__str__()}; Среда обитания: {self.place}; Дата нахождения: {self.date}; Вожак стаи"
        else:
            return f"{super().__str__()} Среда обитания: {self.place}; Дата нахождения: {self.date};"