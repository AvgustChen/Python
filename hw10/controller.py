import model
import view
from fabricCreateAnimal import FabricCreateAnimal as fca


def start():
    num = view.menu()
    match num:
        case 1:
            addAnimal()
        case 2:
            deleteAnimal()
        case 3:
            infoAnimal()
        case 4:
            sayAnimal()
        case 5:
            model.showAll()
            start()
        case 6:
            model.sayAll()
            start()
        case 7:
            exit()


def addAnimal():
    num = view.addAnimalMenu()
    if (num > len(fca.all)):
        start()
    else:
        model.addAnimal(num)
        start()


def deleteAnimal():
    model.showAll()
    num = view.deleteAnimalMenu()
    if (num > len(fca.all)):
        start()
    else:
        model.deleteAnimal(num)
        start()


def sayAnimal():
    model.showAll()
    num = view.sayAnimalMenu()
    if (num > len(fca.all)):
        start()
    else:
        model.sayAnimal(num)
        start()


def infoAnimal():
    model.showAll()
    num = view.showAnimalMenu()
    if (num > len(fca.all)):
        start()
    else:
        model.showInfo(num)
        start()
