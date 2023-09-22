# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os
from pathlib import Path


def rename_files(dir_: str, new_name: str = '', count_of_numbers: int = 3, extension: str = 'txt', extension_2: str = '',
                 chars_of_name: tuple = (0, 0)):
    files = os.listdir(dir_)
    os.chdir(dir_)
    file_count = 0
    for i in range(len(files)):
        file_name, file_extension = files[i].split(".")
        new_file_name = ''
        if file_extension in extension:
            file_count += 1
            if chars_of_name != (0, 0):
                new_file_name += file_name[chars_of_name[0]:chars_of_name[1]]
            if new_name != '':
                new_file_name += f'{new_name}_'
            if count_of_numbers > 0:
                new_file_name += '0' * count_of_numbers
                new_file_name = f'{new_file_name[:-len(str(file_count))]}'
                new_file_name += f'{file_count}'
            if extension_2 != '':
                new_file_name += f'.{extension_2}'
            else:
                new_file_name += f'.{file_extension}'
            Path(files[i]).rename(new_file_name)




    return file_count

