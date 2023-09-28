# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
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


@outer(10)
def sum_func(a, b):
    return a + '_' + b

print(sum_func('Первая', 'Вторая'))
print(sum_func(b='три', a='два'))
print(sum_func('Вова', b='china'))