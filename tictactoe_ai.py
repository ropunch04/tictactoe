#Libraries
import pygame as pg

#Constats
W_WIDTH, W_HEIGHT = 600, 600
BG_COLOR = [87, 186, 172]
LINE_COLOR = [72, 158, 146]
X_COLOR = [84, 84, 84]
O_COLOR = [241, 235, 213]
LINE_WIDTH = 15
WIN_WIDTH = 20

#Window Setup
pg.init()
pg.display.set_caption("Tic-Tac-Toe")
screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))

#Methods
def reset_board():
    screen.fill(BG_COLOR)
    pg.draw.line(screen, LINE_COLOR, (W_WIDTH // 3, 0), (W_WIDTH // 3, W_HEIGHT), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (2 * W_WIDTH // 3, 0), (2 * W_WIDTH // 3, W_HEIGHT), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, W_HEIGHT // 3), (W_WIDTH, W_HEIGHT // 3), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, 2 * W_HEIGHT // 3), (W_WIDTH, 2 * W_HEIGHT // 3), LINE_WIDTH)

def draw_x(row, col):
    pg.draw.line(screen, X_COLOR, (25 + (W_WIDTH // 3) * row, 25 + (W_HEIGHT // 3) * col), ((W_WIDTH // 3 - 25) + (W_WIDTH // 3) * row, (W_HEIGHT // 3 - 25) + (W_HEIGHT // 3) * col), LINE_WIDTH)
    pg.draw.line(screen, X_COLOR, (25 + (W_WIDTH // 3) * row, (W_HEIGHT // 3 - 25) + (W_HEIGHT // 3) * col), ((W_WIDTH // 3 - 25) + (W_WIDTH // 3) * row, 25 + (W_HEIGHT // 3) * col), LINE_WIDTH)

def draw_o(row, col):
    pg.draw.circle(screen, O_COLOR, ((W_WIDTH // 3) // 2 + (W_WIDTH // 3) * row, (W_HEIGHT // 3) // 2 + (W_HEIGHT // 3) * col), (W_WIDTH // 3) // 2 - 25, LINE_WIDTH)

#Main Body
reset_board()

running = True
while(running):
    for event in pg.event.get():
        if (event.type == pg.KEYDOWN):
            if (event.key == pg.K_q):
                running = False
        elif (event.type == pg.QUIT):
            running = False
    pg.display.flip()
pg.quit()