# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def create_list(k):
    new_list = []
    for i in range(k + 1):
        new_list.append(random.randint(0, 101))
    return new_list

def create_str(new_list):
    my_list = new_list[::-1]
    result = ''
    for i in range(len(my_list)):
        if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
            if my_list[i] == 1:
                result +=f'x^{len(my_list) - i - 1} + '
            else:
                result += f'{my_list[i]}x^{len(my_list) - i - 1} + '
        elif i == len(my_list) - 2 and my_list[i] != 0:
            if my_list[i] == 1:
                result += 'x + '
            else:
                result += f'{my_list[i]}x + '
        elif i == len(my_list) - 1 and my_list[i] != 0:
            result += f'{my_list[i]} = 0'
        elif i == len(my_list) - 1 and my_list[i] == 0:
            result += ' = 0'
    return result

def write_file(res):
    with open('Result_004-2.txt', 'w') as data:
        data.write(res)


k = int(input('Введите натуральную степень: '))
coef_list = create_list(k)
write_file(create_str(coef_list))