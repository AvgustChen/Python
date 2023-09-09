# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
num1 = input('Введите первую дробь (a/b): ')
num2 = input('Введите вторую дробь (a/b): ')

num1 = num1.split('/')
num2 = num2.split('/')

num1_1 = int(num1[0])
num1_2 = int(num1[1])

num2_1 = int(num2[0])
num2_2 = int(num2[1])

if num1_2 == num2_2:
    result = num1_1 + num2_1
    sum = f"{str(result)}/{num1_2}"
    print('Сумма дробей = ' + sum)
else:
    result = num1_1 * num2_2 + num2_1 * num1_2
    result2 = num1_2 + num2_2
    sum = f"{str(result)}/{str(result2)}"
    print('Сумма дробей = ' + sum)

mult = f"{str(num1_1*num2_1)}/{str(num1_2*num2_2)}"
print('Произведение дробей = ' + mult)

print ({Fraction(num1_1, num1_2)})
# тут только разобрался во Fraction и получается далее аналогично весь код переписывать для проверки?


