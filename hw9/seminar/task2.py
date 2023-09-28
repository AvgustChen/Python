# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
from random import randint
from typing import Callable


def decor(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if 1 < a > 100:
            print(f'Ты ввел число {a} больше допустимого')
            a = randint(1, 100)
        if 1 < b > 10:
            print(f'Ты ввел число {b} больше допустимого')
            b = randint(1, 10)
        return func(a, b)

    return wrapper


@decor
def inner(a, b):
    while b:
        print(f'У тебя {b} попыток')
        guess = int(input('Введите число: '))
        b -= 1
        if guess < a:
            print(f'Загаданное число больше! Осталось {b} попыток')
        elif guess > a:
            print(f'Загаданное число меньше! Осталось {b} попыток')
        elif guess == a:
            print(f'Вы угадали! Было загадано {a}')
            break

    else:
        print('Вы проиграли! Попыток больше нет!')


inner(200, 20)
