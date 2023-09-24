# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import pickle
import os

def json_to_pickle():
    files = os.listdir()

    for item in range(len(files)):
        file_name, file_extension = files[item].split(".")
        if 'json' in file_extension:
            file_name = f'{file_name}.pickle'
            with open(files[item], 'r', encoding='UTF-8') as file_in:
                my_dict = json.load(file_in)
            with open(file_name, 'wb') as file:
                pickle.dump(my_dict, file)


json_to_pickle()