# Напишите рограмму, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Input number quorter: '))

if num < 1 or num > 4:
    print('Try again!')
elif num == 1:
    print(f'If quorter {num} then [x > 0; y > 0]')
elif num == 2:
    print(f'If quorter {num} then [x < 0; y > 0]')
elif num == 3:
    print(f'If quorter {num} then [x < 0; y < 0]')
else:
    print(f'If quorter {num} then [x > 0; y < 0]')
