# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
import json
import os
from random import randint
from typing import Callable


def outer(count: int):
    def decor(func: Callable):
        data = []

        def wrapper(*args, **kwargs):
            for _ in range(count):
                data.append(func(*args, **kwargs))

            return data

        return wrapper

    return decor


def control(func: Callable) -> Callable:
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


def decor(func: Callable):
    def wraaper(*args, **kwargs):
        file_name = func.__name__ + '.json'
        data = {}
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        result = func(*args, **kwargs)
        data[result.__repr__()] = {'args': args, 'kwargs': kwargs}
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return result

    return wraaper


@outer(2)
@decor
@control
def guess_number(a, b):
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
            return f'Вы угадали! Было загадано {a}'


    print('Вы проиграли! Попыток больше нет!')
    return f'Не угадал! былор загаданно {a}'


guess_number(200, 20)
