# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import csv
import json
import os
import pickle
from pathlib import Path


def walking(path: str):
    file_list = os.walk(path)
    result = {}
    count = 1
    for item in file_list:
        for j in range(len(item)):
            if item[0] in result:
                if type(item[j]) != list:
                    result[f'{item[j]}'].append(item[j])
                if type(item[j]) == list and len(item[j]) > 0:
                    for k in range(len(item[j])):
                        result[f'{item[0]}'].append([item[j][k]])

            else:
                result[item[0]] = []
        count += 1

    for key, value in result.items():
        for j in range(len(value)):
            link = f'{key}\\'
            if '.' in value[j][0]:
                value[j].append('File')
                value[j].append(os.path.getsize(f'{link}{value[j][0]}'))
            else:
                value[j].append('Folder')
                value[j].append(len(os.listdir(f'{link}{value[j][0]}')))
    return result


def to_json(dict_: dict):
    with open('task1.json', 'w', encoding='UTF-8') as file:
        json.dump(dict_, file, indent=4)


def to_csv(dict_: dict):
    result = []
    for key, files in dict_.items():
        result.append([key, files])
    with open('task1.csv', 'w', encoding='UTF-8') as file:
        csv_writer = csv.writer(file, dialect='excel', delimiter='|', lineterminator='\n')
        csv_writer.writerows(result)


def to_pickle(dict_: dict):
    with open('task1.pickle', 'wb') as file:
        pickle.dump(dict_, file)


link = Path.cwd()
dict_1 = walking(link)
to_json(dict_1)
to_csv(dict_1)
to_pickle(dict_1)
