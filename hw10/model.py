import copy
import classes
from fabricCreateAnimal import FabricCreateAnimal as fca


def showAll():
    for i in range(len(fca.all)):
        print(f"{i+1}) {fca.all[i]}")


def showInfo(num):
    print(f"{num-1}) {fca.all[num-1]}")
    if (isinstance(fca.all[num-1], classes.Home)):
        fca.all[num-1].caressing()
    if (isinstance(fca.all[num-1], classes.DogTraining)):
        fca.all[num-1].training()
    if (isinstance(fca.all[num-1], classes.BirdFly)):
        fca.all[num-1].birdFly()


def sayAll():
    for i in range(len(fca.all)):
        fca.all[i].animalSay()


def sayAnimal(num):
    fca.all[num-1].animalSay()


def addAnimal(num):
    match num:
        case 1:
            addCat()
        case 2:
            addTiger()
        case 3:
            addDog()
        case 4:
            addWolf()
        case 5:
            addHen()
        case 6:
            addStork()


def addCat():
    name = "Кот"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    name2 = input("Кличка: ")
    breed = input("Порода: ")
    vaccination = input("Наличие прививки: ")
    color = input("Цвет: ")
    date = input("Дата рождения: ")
    wool = input("Наличие шерсти: ")
    animal = classes.Cat(name, height, weight, colorEye,
                         name2, breed, vaccination, color, date, wool)
    fca.all.append(copy.copy(animal))


def addTiger():
    name = "Тигр"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    place = input("Среда обитания: ")
    date = input("Дата обнаружения: ")
    animal = classes.Tiger(name, height, weight, colorEye, place, date)
    fca.all.append(copy.copy(animal))


def addDog():
    name = "Собака"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    name2 = input("Кличка: ")
    breed = input("Порода: ")
    vaccination = input("Наличие прививки: ")
    color = input("Цвет: ")
    date = input("Дата рождения: ")
    wool = input("Наличие шерсти: ")
    animal = classes.Dog(name, height, weight, colorEye,
                         name2, breed, vaccination, color, date, wool)
    fca.all.append(copy.copy(animal))


def addWolf():
    name = "Волк"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    place = input("Среда обитания: ")
    date = input("Дата обнаружения: ")
    leader = bool(input("Вожак стаи? True/False: "))
    animal = classes.Wolf(name, height, weight, colorEye, place, date, leader)
    fca.all.append(copy.copy(animal))


def addHen():
    name = "Курица"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    fly = 0
    animal = classes.Hen(name, height, weight, colorEye, fly)
    fca.all.append(copy.copy(animal))


def addStork():
    name = "Аист"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    fly = int(input("Высота полета: "))
    animal = classes.Stork(name, height, weight, colorEye, fly)
    fca.all.append(copy.copy(animal))


def deleteAnimal(num):
    fca.all.pop(num-1)