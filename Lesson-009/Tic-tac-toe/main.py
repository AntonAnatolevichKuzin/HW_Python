import emoji
import random
import sys


def maps_print(maps):
    for i in range(len(maps)):
        if i == 2 or i == 5:
            print(maps[i], '   ')
        else:
            print(maps[i], '  ', end='  ')
    print()


def winner(maps, win_res):
    win = ''
    for i in win_res:
        if maps[i[0]] == emoji.emojize(chr(10060)) and maps[i[1]] == emoji.emojize(chr(10060)) and maps[i[2]] == \
                emoji.emojize(chr(10060)):
            win = emoji.emojize(chr(10060))
        elif maps[i[0]] == emoji.emojize(chr(11093)) and maps[i[1]] == emoji.emojize(chr(11093)) and maps[i[2]] == \
                emoji.emojize(chr(11093)):
            win = emoji.emojize(chr(11093))
    return win


def symbol_input(symbol):
    step = int(input('Ваш ход! '))
    flag = False
    while flag != True:
        if step in maps:
            ind = maps.index(step)
            maps[ind] = symbol
            flag = True
        else:
            step = int(input('Эта ячейка занята! Введите другую: '))


maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_res = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

maps_print(maps)
game_over = True
user1 = input('Имя первого игрока: ')
user2 = input('Имя второго игрока: ')
flag = random.randint(0, 1)
if flag == True:
    print(f"Первый ходит {user1}")
else:
    print(f"Первый ходит {user2}")
count = 0
while game_over != False:
    if flag == True:
        symbol = emoji.emojize(chr(10060))
        print(user1, end=' ')
        symbol_input(symbol)
        flag = False
    else:
        symbol = emoji.emojize(chr(11093))
        print(user2, end=' ')
        symbol_input(symbol)
        flag = True

    win = winner(maps, win_res)
    count += 1
    if win == '':
        game_over = True
    else:
        game_over = False
    print(maps_print(maps))

    if count == 9:
        sys.exit('Ничья!')

if win == emoji.emojize(chr(10060)):
    print(f' Победил {user1}!')
else:
    print(f' Победил {user2}!')
