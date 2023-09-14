# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
            if type(value) == list or type(value) == dict or type(value) == tuple:
                result[str(value)] = key
            else:
                result[value] = key
    return result


print(kwargs_to_dict(big='стол', num=6, lst=[1,2,3], my_tuple=(1,2,3), my_dict={'dict': 'my new dick'}))