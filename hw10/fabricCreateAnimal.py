import classes
import copy

class FabricCreateAnimal:
    all = []
    animal = classes.Wolf("Волк", 100, 220, "Зеленые", "Россия", "12.04.1986", True)
    all.append(copy.copy(animal))
    animal = classes.Wolf("Волк", 120, 150, "Голубые", "Европа", "21.12.2014", False)
    all.append(copy.copy(animal))
    animal = classes.Cat("Кот", 15, 3, "Серые", "Мейсон", "Британский вислоухий", "да", "Серый", "07.01.2023", "да")
    all.append(copy.copy(animal))
    animal = classes.Dog("Собака", 45, 24, "Карие", "Бобик", "Двортерьер", "Нет", "Комстромской", "Неизвестно",
                         "Да")
    all.append(copy.copy(animal))
    animal = classes.Hen("Курица", 35, 2, "Желтые", 0)
    all.append(copy.copy(animal))
    animal = classes.Stork("Аист", 55, 4, "Желтые", 35)
    all.append(copy.copy(animal))