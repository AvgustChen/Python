# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import math
import json
import csv
import os
from typing import Callable
from random import choice as ch
from random import randint as ri
from functools import wraps


def generation_csv_file(func: Callable):
    file_name = func.__name__ + '.csv'
    with open(file_name, 'w', encoding='UTF-8') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for i in range(ri(100, 1000)):
            csv_writer.writerow((ch([i for i in range(-100,100) if i != 0]), ch([i for i in range(-100,100) if i != 0]),
                                 ch([i for i in range(-100,100) if i != 0])))


def read_csv(func: Callable):
    generation_csv_file(func)
    file_name = func.__name__ + '.csv'
    @wraps(func)
    def wrapper():
        nonlocal file_name
        with open(file_name, 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for i in data:
                if i:
                    func(*i)

    return wrapper


def json_result(func: Callable):
    result = {}
    file_name = func.__name__ + '.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:
            result = json.load(file)

    @wraps(func)
    def wrapper(*args):
        a, b, c, *_ = args
        equation = func(a, b, c)
        result[f'{a}, {b}, {c}'] = equation
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(result, file, indent=4)
        return equation

    return wrapper


@read_csv
@json_result
def square_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return (f'x1 = {round(x1, 2)}\n'
                f'x2 =  {round(x2, 2)}')
    elif discr == 0:
        x = -b / (2 * a)
        return f'x = {round(x, 2)}'
    else:
        return 'Not squares'


square_equation()
