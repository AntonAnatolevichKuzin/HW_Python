# Создайте программу для игры в ""Крестики-нолики"".
import random
import sys

def maps_print(maps):
    for i in range(len(maps)):
        if i == 2 or i == 5:
            print(maps[i],' ')
        else:
            print(maps[i],' ', end=' ')
    print()

def winner(maps, win_res):
    win = ''
    for i in win_res:
        if maps[i[0]] == 'x' and maps[i[1]] == 'x' and maps[i[2]] == 'x':
            win = 'x'
        elif maps[i[0]] == '0' and maps[i[1]] == '0' and maps[i[2]] == '0':
            win = '0'
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
win_res = ([0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [2, 4, 7], [3, 5, 8], [0, 4, 8], [2, 4, 6])

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
        symbol = 'x'
        print(user1, end=' ')
        symbol_input(symbol)
        flag = False       
    else:
        symbol = '0'
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
        
if win == 'x':
    print(f' Победил {user1}!')
else:
    print(f' Победил {user2}!')



# import random
# from tkinter import *

# root = Tk()         # делаем окно с заголовком
# root.title('Крестики-нолики')

# game_run = True     # если будет победитель, будет False
# field = []          # в массиве храним состояние поля
# cross_count = 0     # Подсчитываем количество крестиков на поле, максимально 5


# def new_game():     # поле и переменные обнуляются
#     for row in range(3):
#         for col in range(3):
#             field[row][col]['text'] = ' '
#             field[row][col]['background'] = 'lavender'
#     global game_run
#     game_run = True
#     global cross_count
#     cross_count = 0


# def click(row, col):        # ставим крестик и считаем
#     if game_run and field[row][col]['text'] == ' ':
#         field[row][col]['text'] = 'X'
#         global cross_count
#         cross_count += 1
#         check_win('X')      # проверка на победу
#         if game_run and cross_count < 5:
#             computer_move()
#             check_win('O')  # проверка на победу

# # проверка победы по всем направлениям


# def check_win(smb):
#     for n in range(3):
#         check_line(field[n][0], field[n][1], field[n][2], smb)
#         check_line(field[0][n], field[1][n], field[2][n], smb)
#     check_line(field[0][0], field[1][1], field[2][2], smb)
#     check_line(field[2][0], field[1][1], field[0][2], smb)

# # на входе три поля и символ, если символ есть в этих трех полях,
# # то меняем цвет полей на розовый и остановка игры


# def check_line(a1, a2, a3, smb):
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
#         a1['background'] = a2['background'] = a3['background'] = 'pink'
#         global game_run
#         game_run = False


# def can_win(a1, a2, a3, smb):   # проверка на победу
#     res = False
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
#         a3['text'] = 'O'
#         res = True
#     if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
#         a2['text'] = 'O'
#         res = True
#     if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
#         a1['text'] = 'O'
#         res = True
#     return res


# def computer_move():
#     for n in range(3):
#         if can_win(field[n][0], field[n][1], field[n][2], 'O'):
#             return
#         if can_win(field[0][n], field[1][n], field[2][n], 'O'):
#             return
#     if can_win(field[0][0], field[1][1], field[2][2], 'O'):
#         return
#     if can_win(field[2][0], field[1][1], field[0][2], 'O'):
#         return

#     while True:  # случ. образом перебираются поля, пока не выпадет свободное
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
#         if field[row][col]['text'] == ' ':
#             field[row][col]['text'] = 'O'
#             break


# for row in range(3):  # создаем поле кнопок
#     line = []
#     for col in range(3):
#         button = Button(text=' ', width=6, height=3,
#                         font=('Verdana', 22, 'bold'),
#                         background='lavender',
#                         command=lambda row=row, col=col: click(row, col))
#         button.grid(row=row, column=col, sticky='nsew')
#         line.append(button)
#     field.append(line)

# new_button = Button(text='Новая игра', command=new_game)
# new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

# root.mainloop()