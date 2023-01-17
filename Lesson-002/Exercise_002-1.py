# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# digit = float(input('Enter digit: '))
# print(f'{digit} -> ', end='')
# sum = 0
# for i in str(digit):
#   if i != '.':
#     sum += int(i)
# print(sum)

digit = input('Enter digit: ')
print(f'{digit} -> ', end='')
sum = 0
for i in digit:
  if i.isdigit(): #Подсказка ревьюера !!!
    sum += int(i)
print(sum)

