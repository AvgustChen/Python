# Создайте функцию генератор чисел Фибоначчи

def gen_fib(n):
    fib = [0, 1]
    count = 0
    while count < n:
        fib.append(fib[-2] + fib[-1])
        yield fib[-2]
        count += 1

print(*gen_fib(10))