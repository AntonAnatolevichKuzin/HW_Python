# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Input number: '))
print(f'{num} -> ', end='')
binar = ''
while num > 0:
    binar = str(num % 2) + binar
    num = num // 2
print(binar)

# Еще один вариант

# Four
from os import system


def console_clear():
    system('cls')


def dec_to_bin1(num: int):   # Способ 1 (с помощью списка)
    n_bin = list()
    if num == 0:
        n_bin.append(0)
        return n_bin
    while num > 0:
        n_bin.append(num % 2)
        num //= 2
    n_bin.reverse()
    return n_bin


def dec_to_bin2(num: int):  # Способ 2 (с помощью строки)
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result

print('Программа переводит целое десятичное число в двоичное')
num = int(input('Введите целое число: '))
msg = f'{num} ->'
print(msg, ''.join(map(str, dec_to_bin1(num))))
print(msg, dec_to_bin2(num))
print(msg, bin(num)[2:])  # Способ 3 (с помощью встроенной функции)


