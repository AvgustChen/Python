# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def readfile():
    with open('task1.txt', 'r') as f:
        my_dict = {}
        for i in f:
            tmp = i.split('|')
            my_dict[tmp[0]] = tmp[1][:-2].title()
    return my_dict


def to_json(my_dict):
    with open('task1.json', 'w') as f:
        json.dump(my_dict, f, separators=[', \n', ': '])


my_dict = readfile()
to_json(my_dict)
