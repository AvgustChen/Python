# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json


def csv_read(file1: str, file2: str):
    data = {}
    with open(file1, 'r') as csv_file:
        for i in csv_file:
            tmp = i.split('|')
            tmp[1] = tmp[1].zfill(10)
            if tmp[2][:-1] in data:
                data[tmp[2][:-1]].append({tmp[1]: (tmp[0].lower(), hash(tmp[1] + tmp[0].lower()))})
            else:
                data[tmp[2][:-1]] = [{tmp[1]: (tmp[0].lower(), hash(tmp[1] + tmp[0].lower()))}]
    with open(file2, 'w') as file:
        json.dump(data, file, indent=1)




csv_read('task3.csv', 'task4.json')