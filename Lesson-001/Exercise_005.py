#  Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.
from math import sqrt
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xA = int(input('Input coordinate "X" 1-th point: '))
yA = int(input('Input coordinate "Y" 1-th point: '))
xB = int(input('Input coordinate "X" 2-th point: '))
yB = int(input('Input coordinate "Y" 1-th point: '))

print(f'A({xA},{yA}); B({xB},{yB}) -> ', end='')
distance = sqrt((xB-xA)**2 + (yB-yA)**2)
print(round(distance, 3))

# Еще один вариатн решения задачи 

x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by space - ').split()))
x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by space - ').split()))

print(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3))
