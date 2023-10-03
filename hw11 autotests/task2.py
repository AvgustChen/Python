# Разработайте программу для хранения и управления текстовыми и числовыми записями.
# Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:
#
# Класс Archive должен иметь следующие атрибуты:
#
# archive_text (list): Список архивированных текстовых записей.
# archive_number (list): Список архивированных числовых записей.
# text (str): Текущая текстовая запись, которую нужно добавить в архив.
# number (int или float): Текущая числовая запись, которую нужно добавить в архив.
# Класс Archive должен реализовать шаблон Singleton, чтобы гарантировать, что существует только один экземпляр архива.
#
# Класс Archive должен иметь метод __init__(self, text: str, number: int | float), который принимает текстовую и
# числовую запись и сохраняет их как текущие записи для добавления в архив.
#
# Класс Archive должен реализовать методы
# __str__(self) и __repr__(self), чтобы можно было получить строковое представление текущих записей и архива.

class Archive:
    _instance = None
    archive_text = []
    archive_number = []
    last_number = None
    last_text = None

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.last_number = number
            cls.last_text = text
        else:
            cls.archive_text.append(cls.last_text)
            cls.archive_number.append(cls.last_number)
            cls.last_number = number
            cls.last_text = text
        return cls._instance

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number



    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive({self.text}, {self.number})"

archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive1)
print(archive3)

