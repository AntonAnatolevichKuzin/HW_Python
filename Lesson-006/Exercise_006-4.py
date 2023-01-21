# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Использование функции "enumerate"

import random

my_list = [random.randint(0, 10) for i in range(1, 8)]
print(f'{my_list} -> на нечетных позициях элементы ', end='')
new_list = [v for k, v in enumerate(my_list) if k % 2]
print(new_list, end=' ')
res = sum(new_list)
print(f'ответ: {res}')
