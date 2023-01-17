# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
import random

my_list = []
for i in range(0, 8):
    my_list.append(random.randint(0, 10))
print(my_list)
corr_list = []
unic_num = set(my_list)
for my_list in unic_num:
    corr_list.append(my_list)
print(corr_list)
