# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def str_way(string: str):
    expansion = string.split('.')
    way_name = expansion[0].split('/')
    way = way_name[0]
    name = way_name[-1]
    for i in range(1, len(way_name) - 1):
        way += (f'/{way_name[i]}') 

    return way, name, expansion[-1],      

    
    

string = 'E:/Unity/done/Zombie arcade.exe'
print(str_way(string))