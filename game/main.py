import pygame as pg
from pygame.locals import *
import time

def draw_board(arr):
    for i in range(29):
        pg.draw.line(screen, (0, 0, 0), ((i + 1) * 20, 0), ((i + 1) * 20, 600))
        pg.draw.line(screen, (0, 0, 0), (0, (i + 1) * 20), (600, (i + 1) * 20))

        for c in range(30):
            for r in range(30):
                if arr[c][r] == 0:
                    # pg.draw.rect(screen, (0, 0, 0), Rect(c*20, r*20, 20, 20))
                    screen.blit(grass, (c*20, r*20))
                elif arr[c][r] == 1:
                    # pg.draw.rect(screen, (255, 255, 255), Rect(c * 20, r * 20, 20, 20))
                    screen.blit(ppl, (c* 20, r*20))
                else:
                    screen.blit(house, (c*20, r*20))

pg.init()

screen = pg.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pg.display.flip()

rows, cols = (60, 60)
board = [[0 for i in range(cols)] for j in range(rows)]

board[1][5] = 1
board[23][6] = 1
board[17][8] = 2
board[3][27] = 1
board[7][4] = 1
board[2][25] = 1
board[22][15] = 2
board[15][19] = 1
board[11][26] = 1
board[13][29] = 2
board[18][11] = 1

grass = pg.image.load("grass_textr.png")
ppl = pg.image.load("creepy_ppl.png")
house = pg.image.load("house.png")

running = True

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            draw_board(board)

        pg.display.flip()