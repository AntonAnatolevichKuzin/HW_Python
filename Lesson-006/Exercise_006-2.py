#  Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Использованы round и map

import random

my_list = [round((random.random() * 10), 3) for i in range(0, 8)]

print(f'{my_list} => ', end='')

my_list2 = list(map(lambda a: round(a % 1, 3), my_list))

print(max(my_list2) - min(my_list2))
