# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# просто оптимизация кода с 9 строк до 4

import random

my_list = [random.randint(0, 10) for i in range(0, 8)]
print(my_list)
unic_num = list(set(my_list))
print(unic_num)



