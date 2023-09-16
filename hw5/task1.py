# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_numbers(num: int):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

def gen_simple_numbers(n: int):
    count = 0
    number = 2
    result = []
    while count <= n:
        if simple_numbers(number):
            result.append(number)
            yield number
            count += 1
        number += 1


        
lst = gen_simple_numbers(10)
print(*lst)