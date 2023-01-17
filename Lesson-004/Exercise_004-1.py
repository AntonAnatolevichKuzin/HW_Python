# Вычислить число c заданной точностью d
#
# Пример:
#
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import random

exactnes = input('Задайте точность числа из диапазона 10^{-1} ≤ d ≤10^{-10}: ')
dig = (abs(str(exactnes).find('.') - len(str(exactnes))) - 1)
num = float(random.random())
print(f'при d = {exactnes}, число {num}, примет следующий вид: {round(num, dig)}')

