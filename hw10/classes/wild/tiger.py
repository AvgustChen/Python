from .wild import Wild


class Tiger(Wild):
    def __init__(self, name, height, weight, color_eye, place, date):
        super(Tiger, self).__init__(name, height, weight, color_eye, place, date)

    def animalSay(self):
        print(f"{super().animalSay()}  РРРррр")

    def __str__(self) -> str:
        return f"{super().__str__()}; Среда обитания: {self.place}; Дата нахождения: {self.date};"