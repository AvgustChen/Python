# cort = (1, 6, 7, 'text', 5.6, [1, 4, 7, 8], 'text2', [1,5,6,3,7,8,], True, False, 6.2)
# dict = dict()
# for i in cort:
#     if type(i) not in dict:
#         dict[type(i)] = []
#     dict[type(i)].append(i)
# print(dict)
# //////////////////////////////////
# cort = (1, 6, 7, 'text', 5.6, [1, 4, 7, 8], 'text2', [1,5,6,3,7,8,], True, False, 6.2)
# dict = dict()
# for i in cort:
#     dict.setdefault(type(i),[])
#     dict[type(i)].append(i)
# print(dict)
# /////////////////////////////////////



# list = [1,2,5,4,6,2,3,1,4,3,3,3,2,5,6,7,3,4]
# for i in list:
#     if (count:=list.count(i)) >= 2:
#         for _ in range(count//2):
#             list.remove(i)
#             list.remove(i)
# print(list)
# //////////////////////////////////



# text = 'У лукоморья дуб зеленный, золотая цепь на дубе том'
# text = text.split(' ')
# len_max = max(text, key=len)
# len_max = len(len_max)
# text.sort()
# for i, word in enumerate(text, 1):
#     print(f"{i}. {word :>{len_max}}")






# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# # или не совпадают в ваших решениях.

# text = 'У лукоморья дуб зеленный, золотая цепь на дубе том'
# my_dict = dict()

# for i in text:
#     my_dict[i] = my_dict.get(i, 0) + 1
# print(my_dict)

# for i in set(text):
#     my_dict[i] = text.count(i)
# print(my_dict)

















    

