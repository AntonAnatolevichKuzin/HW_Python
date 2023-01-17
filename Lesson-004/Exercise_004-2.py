#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите натуральное число: '))
multipliers = []
d = 2
m = num
while d * d <= m:
    if m % d == 0:
        multipliers.append(d)
        m //= d
    else:
        d += 1
multipliers.append(m)
print(f'Простые множители числа {num} => {multipliers}')