#1 - Human
#2 - Computer

import time
import random
import pygame as pg
import numpy as np

#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BG_COLOR = [87,  186, 172]
LINE_COLOR = [72, 158, 146]
X_COLOR = [84, 84, 84]
O_COLOR = [241, 235, 213]
LINE_WIDTH = 20

#Window Creation
pg.init()
pg.display.set_caption("Tic-Tac-Toe")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Methods
def reset_board():
    screen.fill(BG_COLOR)
    pg.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), 15)
    pg.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), 15)
    pg.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), 15)
    pg.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), 15)
    return np.zeros((3, 3))

def draw_x(row, col):
    pg.draw.line(screen, X_COLOR, (25 + 200 * row, 25 + 200 * col), (175 + 200 * row, 175 + 200 * col), 15)
    pg.draw.line(screen, X_COLOR, (25 + 200 * row, 175 + 200 * col), (175 + 200 * row, 25 + 200 * col), 15)

def draw_o(row, col):
    pg.draw.circle(screen, O_COLOR, (100 + 200 * row, 100 + 200 * col), 75, 15)

def mark_square(row, col, player):
    if user_input == 1:
        if player == 1:
            draw_x(row, col)
        elif player == 2:
            draw_o(row, col)
    elif user_input == 2:
        if player == 1:
            draw_o(row, col)
        elif player == 2:
            draw_x(row, col)
    board[row][col] = player

def available(row, col):
    return board[row][col] == 0

def filled():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def winner(player):
    check = ''
    board_flip = board
    #horizontal check (transpose)
    for col in range(3):
        if board_flip[0][col] == player and board_flip[1][col] == player and board_flip[2][col] == player:
            check, num = 'hor', col
    #vertical check (transpose)
    for row in range(3):
        if board_flip[row][0] == player and board_flip[row][1] == player and board_flip[row][2] == player:
            check, num = 'ver', row 
    #diagnol check
    if board_flip[0][0] == player and board_flip[1][1] == player and board_flip[2][2] == player:
        check, num = 'asc', None
    elif board_flip[0][2] == player and board_flip[1][1] == player and board_flip[2][0] == player:
        check, num = 'desc', None
    if check == '':
        return False
    else:
        draw_winline(check, num, player, user_input)
        return True

def draw_winline(check, num, player, starting_player):
    if starting_player == 1:
        colors = {
            1 : X_COLOR,
            2 : O_COLOR
        }
    elif starting_player == 2:
        colors = {
            1 : O_COLOR,
            2 : X_COLOR
        }
    win_color = colors.get(player)

    if check == 'ver':
        pg.draw.line(screen, win_color, (100 + 200 * num, 0), (100 + 200 * num, 600), LINE_WIDTH)
    elif check == 'hor':
        pg.draw.line(screen, win_color, (0, 100 + 200 * num), (600, 100 + 200 * num), LINE_WIDTH)
    elif check == 'desc':
        pg.draw.line(screen, win_color, (0, 600), (600, 0), LINE_WIDTH)
    elif check == 'asc':
        pg.draw.line(screen, win_color, (0, 0), (600, 600), LINE_WIDTH)

#Main Body of Code
board = reset_board()
proper_selection = False
while (not proper_selection):
    user_input = input("Would you like to be X or O?").lower()
    if user_input == 'x':
        proper_selection = True
        user_input = 1
    elif user_input == 'o':
        proper_selection = True
        user_input = 2
    else:
        print("Please choose either X or O!")
current_player = user_input

running = True
while(running):
    bool1 = False
    bool2 = False
    for event in pg.event.get():
        if (event.type == pg.KEYDOWN):
            if (event.key == pg.K_q):
                running = False
        elif (event.type == pg.QUIT):
            running = False
        elif (event.type == pg.MOUSEBUTTONDOWN):
            if current_player == 1:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseX // 200
                clicked_col = mouseY // 200

                if available(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, 1)
                    current_player = 2

    bool1 = winner(1)
    
    if current_player == 2 and not filled() and not bool1:
        taken = True
        while(taken):
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)
            if available(rand_row, rand_col):
                mark_square(rand_row, rand_col, 2)
                taken = False
    current_player = 1

    bool2 = winner(2)

    pg.display.flip()
    if bool1 or bool2 or filled():
        time.sleep(1.5)
        board = reset_board()
        current_player = user_input
pg.quit()
