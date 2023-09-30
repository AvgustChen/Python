# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Human:

    def __init__(self, last_name, name, fathers_name, age):
        self.last_name = last_name
        self.name = name
        self.fathers_name = fathers_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f"'ФИО:' {self.last_name}, {self.name}, {self.fathers_name}"

    def show_age(self):
        return self.__age

# man = Human('Chen', 'Avgust', 'Vladimirovich', 37)

# print(man.full_name())
# print(man.show_age())
# man.birthday()
# print(man.show_age())
