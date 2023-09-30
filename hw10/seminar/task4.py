# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from task3 import Human
from random import randint as ri


class Employee(Human):

    def __init__(self, id_user, last_name, name, fathers_name, age):
        super().__init__(last_name, name, fathers_name, age)
        self.id_user = id_user
        self.user_access = int(sum(list(map(int, str(id_user)))) % 7)


man = Employee(ri(100000, 999999), 'Chen', 'Avgust', 'Vladimirovich', 37, )
print(man.user_access)
print(man.id_user)
