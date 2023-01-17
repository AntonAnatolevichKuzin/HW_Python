# 5. Реализуйте алгоритм перемешивания списка.

import random

my_list = []
for i in range(1, 8):
    my_list.append(random.randint(-5, 5))
print(my_list)

for i in range(0, len(my_list)):
    if i < len(my_list) - 1:
        temp = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = temp



print(my_list)

# Еще решение

import random


def list_shuffle(_list: list):
    shuffled_list = []
    temp_list = _list.copy()

    for _ in range(len(_list)):
        position = random.randint(0, len(temp_list) - 1)
        elem = temp_list.pop(position)
        shuffled_list.append(elem)
    return shuffled_list


print(list_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
