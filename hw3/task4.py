# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
import random
def take_things(bag_size: int):
    bag = {}
    while bag_size > 0:
        new_key = random.choice(list(THINGS.keys()))
        if THINGS[new_key] <= bag_size:
            bag[new_key] = bag.get(new_key, 0) + 1
        bag_size -= THINGS[new_key]
    return bag

THINGS = {"палатка": 6,
          "котелок": 2,
          "посуда": 2,
          "ложки": 1,
          "вилки": 1,
          "продукты": 5,
          "вода": 2,
          "фонарик": 1,
          "спички": 1,
          }
bag_size = int(input('Введите размер рюкзака: '))
bag = take_things(bag_size)
count = 1
for key, value in bag.items():
    print(f"{count}. {key} - {value} штук")
    count += 1




