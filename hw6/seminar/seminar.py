# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать его за
# заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если
# попытки исчерпаны - ложь.
import sys
from f06 import guess_game

if __name__ == '__main__':
    options = list(map(int, sys.argv[1:]))
    low_limit = 1
    high_limit = 100
    count = 10
    if len(options):
        if len(options) == 1:
            high_limit = options[0]
        elif len(options) == 2:
            low_limit, high_limit = options
        else:
            low_limit, high_limit, count = options
guess_game(low_limit, high_limit, count)
