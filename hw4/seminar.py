# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# def words (text: str):
#     text = text.lower().split(' ')
#     text.sort()
#     len_max = len(max(text, key=len))
#     for item, word in enumerate(text, 1):
#         print(f"{item}. {word :>{len_max}}")

# text = 'У лукоморья дуб зеленый, золотая цепь на дубе том'
# words(text)       

# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def words(text: str):
#     codes = []
#     for i in set(text):
#         codes.append(ord(i))
#     codes.sort(reverse=True)
#     return codes

# text = 'У лукоморья дуб зеленый'

# print(words(text))

# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def unicode_to_char(text: str):
#     result = {}
#     text = text.split()
#     for i in range(len(text)):
#         text[i] = int(text[i])
#     text.sort()
#     for num in range(text[0], text[1] + 1):
#         result[chr(num)] = num
#     return result

# text = '230 45'
# print(unicode_to_char(text))

# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# def buble_sort(lst: list):
#     for i in range(1, len(lst)):
#         for j in range(len(lst)-i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst

# print(buble_sort(lst:=[12,45,23,94,165,29,877,34,65,16]))

# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

# def get_dict(lst_name, lst_stv, lst_prem):
#     return {lst_name[i]: lst_stv[i] * float(lst_prem[i][:-1])/100 for i in range(len(lst_name))}

# print(get_dict(["Иван","Андрей","Сергей"],[1000, 2000, 1500], ["12.6%","9.5%","11%"]))

# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

# def func(lst: list[int], lower: int, upper: int):
#     result = 0
#     for i in range(0 if lower < 0 else lower, len(lst) if upper > len(lst) else upper):
#         result += lst[i]
#     return result

# print(func([12, 43, 23, 2, 1, 5, 6], 2, 46))

# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# import random


# comapanies = {name: [random.randint(-10000, 10000) for _ in range(random.randint(3,10))]
#                for name in ['adibas', 'hike', 'rybok']}
# print(comapanies)

# def func(dct_comp: dict)-> bool:
#     for i in dct_comp:
#         dct_comp[i] = sum(dct_comp[i])
#     return all(map(lambda x: x>0, dct_comp.values()))

# print(func(comapanies))

# ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# ✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s 
# (кроме переменной из одной буквы s) на None. ✔Значения не удаляются, а помещаются в одноимённые 
# переменные без s на конце.

start = 100
s = 'letter'
apples = 25
codes = 10010110111011

def func():
    temp_dict = {}
    for item in globals():
        if not item.startswith('__'):
            if item.endswith('s') and len(item) > 1:
                temp_dict[item[:-1]] = globals()[item]
                temp_dict[item] = None
    globals().update(temp_dict)


func()
print([item for item in globals().items() if not item[0].startswith('__')])



