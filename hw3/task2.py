# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = [1,5,6,8,3,4,4,6,8,8,2,2,4,1]
out_list = []

for i in my_list:
    if my_list.count(i) >= 2 and i not in out_list:
        out_list.append(i)

print(out_list)
