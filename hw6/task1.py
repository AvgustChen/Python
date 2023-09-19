# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

from date import check_date

date = check_date('31.02.2000')
print('Дата может существовать' if date else 'Такая дата невозможна')
