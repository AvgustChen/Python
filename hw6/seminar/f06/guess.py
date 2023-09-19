from random import randint as ri


def guess_game(down_num=0, upper_num=100, count=5):
    number = ri(down_num, upper_num + 1)

    while count:
        num = int(input(f'Введите число от {down_num} до {upper_num}:'))
        if num > number:
            print('Меньше')
            count -= 1
        elif num < number:
            print('Больше')
            count -= 1
        else:
            print('Вы угадали!')
            break
    if count == 0:
        print('Вы проиграли, попыток больше нет!')
