# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def json_to_csv():
    with open('task2.json', 'r') as f_j:
        my_dict = json.load(f_j)

    result = []
    for access, users in my_dict.items():
        for user in users:
            for u_id, name in user.items():
                result.append([name, u_id, access])
    with open('task3.csv', 'w') as f_c:
        csv_writer = csv.writer(f_c, dialect='excel', delimiter='|', lineterminator='\n')
        csv_writer.writerows(result)


json_to_csv()