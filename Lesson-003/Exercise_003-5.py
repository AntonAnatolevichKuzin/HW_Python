#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Input number: '))
print(f'для к = {num} список будет выглядеть так: ', end='')

fib_list = []
for i in range(0, num + 1):
    if i == 0:
        fib_list.append(0)
    elif i == 1 or i == 2:
        fib_list.append(1)
    else:
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

neg_fib_list = []
for n in range(1, num + 1):
    neg_fib_list.insert(0, int(((-1) ** (n + 1)) * fib_list[n]))
result = neg_fib_list + fib_list
print(result)

# Five

def fib(n):
    fib_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i %2 else x)
    return fib_list

fib_num = int(input('Input number: '))
print(f'для k = {fib_num} список будет выглядеть так: {fib(fib_num)}')