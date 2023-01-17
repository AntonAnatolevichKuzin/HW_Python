# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Enter X value: '))
# y = int(input('Enter Y value: '))
# z = int(input('Enter Z value: '))

# print(not (x and y and z) == (not (x) or not (y) or not (z)))

for x in [1, 0]:
    for y in [1, 0]:
        for z in [1, 0]:
            print(x, y, z)
            print(not( x or y or z)) == (not x and not y and not z)
            
