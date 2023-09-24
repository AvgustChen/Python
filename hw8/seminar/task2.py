# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
import os


def add_users():
    while True:
        if os.path.exists('task2.json'):
            with open('task2.json', 'r') as f:
                my_dict = json.load(f)
                print(my_dict)
        else:
            my_dict = {}

        user = input('Введите ваше имя: ')
        if user == 'e':
            break
        u_id = input('Введите ID: ')
        access = input('введите уровень доступа (1-7): ')
        if access in my_dict:
            tmp = my_dict[access]
            tmp.append({u_id: user})
            my_dict[access] = tmp
        else:
            my_dict[access] = [{u_id: user}]

        with open('task2.json', 'w') as f:
            json.dump(my_dict, f, indent=2)


add_users()
