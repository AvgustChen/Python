# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, width, length=None):
        self.width = width
        if length == None:
            self.length = width
        else:
            self.length = length


    def perimeter(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length


rect = Rectangle(2,2)
print(rect.perimeter())
print(rect.area())
