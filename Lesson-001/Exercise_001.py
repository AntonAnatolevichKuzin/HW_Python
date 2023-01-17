# Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

n = int(input('Input number of day of week: '))

if n < 1 or n > 7:
    print('Try again!')
elif n < 6:
    print('No')
else:
    print('Yes')
