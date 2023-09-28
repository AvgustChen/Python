# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
from typing import Callable
import json
import os


def decor(func: Callable):
    def wraaper(*args, **kwargs):
        file_name = func.__name__ + '.json'
        data = {}
        if os.path.isfile(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        result = func(*args, **kwargs)
        data[result] = {'args': args,  'kwargs': kwargs}
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return result

    return wraaper

@decor
def sum_func(a, b):
    return a + '_' + b

print(sum_func('Первая', 'Вторая'))
print(sum_func(b='три', a='два'))
print(sum_func('Вова', b='china'))