# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

NUM_HEX = 16
number = int(input('Введите целое число: '))
number_in_memory = number
result = ' '

11, 12, 13, 14, 15
while number_in_memory:
    if number_in_memory % NUM_HEX == 10:
        result = 'a' + result
    elif number_in_memory % NUM_HEX == 11:
        result = 'b' + result
    elif number_in_memory % NUM_HEX == 12:
        result = 'c' + result
    elif number_in_memory % NUM_HEX == 13:
        result = 'd' + result
    elif number_in_memory % NUM_HEX == 14:
        result = 'e' + result
    elif number_in_memory % NUM_HEX == 15:
        result = 'f' + result
    else:
        result = str(number_in_memory % NUM_HEX) + result
    number_in_memory //= NUM_HEX




print(result)
print(hex(number)[2:])