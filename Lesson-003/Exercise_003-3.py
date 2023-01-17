#  Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []
for i in range(0, 8):
    my_list.append(round((random.random() * 10), 3))
print(f'{my_list} => ', end='')

frac_list = []
for i in range(len(my_list)):
    frac_list.append(round((my_list[i] % 1), 3))
print(max(frac_list) - min(frac_list))

