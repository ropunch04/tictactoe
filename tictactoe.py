import pygame as pg
import numpy as np

#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BG_COLOR = [87,  186, 172]
LINE_COLOR = [72, 158, 146]
X_COLOR = [84, 84, 84]
O_COLOR = [241, 235, 213]

#Window Creation
pg.init()
pg.display.set_caption("Tic-Tac-Toe")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Backend Board Creation
board = np.zeros((3, 3))

#Methods
def create_board():
    screen.fill(BG_COLOR)
    pg.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), 15)
    pg.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), 15)
    pg.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), 15)
    pg.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), 15)

def draw_x(row, col):
    pg.draw.line(screen, X_COLOR, (25 + 200 * row, 25 + 200 * col), (175 + 200 * row, 175 + 200 * col), 15)
    pg.draw.line(screen, X_COLOR, (25 + 200 * row, 175 + 200 * col), (175 + 200 * row, 25 + 200 * col), 15)

def draw_o(row, col):
    pg.draw.circle(screen, O_COLOR, (100 + 200 * row, 100 + 200 * col), 75, 15)

def mark_square(row, col, player):
    if player == 1:
        draw_x(row, col)
    elif player == 2:
        draw_o(row, col)
    board[row][col] = player


def available(row, col):
    return board[row][col] == 0

def filled():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

create_board()
current_player = 1


running = True
while(running):
    for event in pg.event.get():
        if (event.type == pg.KEYDOWN):
            if (event.key == pg.K_q):
                running = False
        elif (event.type == pg.QUIT):
            running = False
        elif (event.type == pg.MOUSEBUTTONDOWN):
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseX // 200
            clicked_col = mouseY // 200

            if available(clicked_row, clicked_col):
                if current_player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    current_player = 2
                elif current_player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    current_player = 1
    pg.display.flip()
pg.quit()


