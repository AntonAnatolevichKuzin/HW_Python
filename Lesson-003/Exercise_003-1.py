# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []
for i in range(1, 8):
    my_list.append(random.randint(0, 10))
# my_list = [5, 7, 3, 9, 1, 8, 2]
print(f'{my_list} -> на нечетных позициях элементы ', end='')
sum = 0
# count = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        sum += my_list[i]
        print(my_list[i], end=' ')
    else:
        continue
print(f'ответ: {sum}')
