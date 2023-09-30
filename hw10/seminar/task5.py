# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
class Dog:
    def __init__(self, name, age, command):
        self.name = name
        self.age = age
        self.command = command

    def show_info(self):
        return f'{self.name} can {self.command}'


class Cat:
    def __init__(self, name, age, sleep_time):
        self.name = name
        self.age = age
        self.sleep_time = sleep_time

    def show_info(self):
        return f'{self.name} can sleep {self.sleep_time} hours'


class Bird:
    def __init__(self, name, age, can_fly):
        self.name = name
        self.age = age
        self.can_fly = can_fly

    def show_info(self):
        if self.can_fly:
            return f'{self.name} can fly'
        else:
            return f"{self.name} can not fly"


pet1 = Dog('Charly', 3, 'sitDown')
pet2 = Cat('Musya', 5, 3)
pet3 = Bird('Chijik', 1, False)

print(pet1.show_info())
print(pet2.show_info())
print(pet3.show_info())