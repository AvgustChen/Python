# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

count = 11

for i in range(count):
    for j in range(count):
        if i > 1 and j > 1 and i < 10:
            if j == 10:
                print(' ')
            else:
                result = i * j
                print(i, '*', j, '=', result)
        


