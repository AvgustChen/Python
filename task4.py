# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import
# randint num = randint(LOWER_LIMIT, UPPER_LIMIT) 
# ТОЛЬКО ДЕЛАЮ ЧТОБ ПРОГРАММА УГАДАЛА!

from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 1000
count = 10
print('Загадайте число от 1 до 1000')

while count > 0:
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print(f"Осталось {count} попыток! Диапозон чисел от {LOWER_LIMIT} до {UPPER_LIMIT}")
    print('Это число', num, '?')
    answer = input('Введите ответ (Больше, Меньше, или Да): ')
    if answer == 'Меньше' or answer == 'меньше':
        UPPER_LIMIT = num
        print(' ')
        count -= 1
    elif answer == 'больше' or answer == 'Больше':
        LOWER_LIMIT = num
        print(' ')
        count -= 1
    elif answer == 'Да' or answer == 'да':
        print('Ура, я угадал Ваше число!')
        break
else:
    print('Увы, я проиграл!')
    






