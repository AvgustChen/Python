# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
from math import pi


class Circke:

    def __init__(self, rad):
        self.rad = rad

    def lenght_c(self):
        return 2 * self.rad * pi

    def area(self):
        return (self.rad * self.rad) * pi


circle_1 = Circke(3)
print(circle_1.lenght_c())
print(circle_1.area())