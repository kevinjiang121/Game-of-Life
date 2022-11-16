"""
 About: Simple Python implementation of John Conway's Game of Life. So far, the game is limited to a 10x10 grid.
 Rules of the Game
 0 -> dead, 1 -> Alive, neighbor-> alive residents of the eight squares surrounding it
 If an alive square have 0-1 neighbors, it dies
 If an alive square have 2-3 neighbors, it lives
 If an alive square have 4 or more neighbors, it dies
 If a dead square have exactly 3 neighbors, it lives
"""
import sys

import numpy as np
from PlayGame import PlayGame
import pygame as pg

N = 100
ALIVE = (0, 0, 0)
DEAD = (255, 255, 255)
HEIGHT = 1080
WIDTH = 1980

g = np.zeros((N, N), dtype=int)
g_temp = np.zeros((N, N), dtype=int)

play = -1


def clear_board():
    for x in range(N):
        for y in range(N):
            g[x, y] = 0
            g_temp[x, y] = 0


def next_loop():
    global g
    plays = PlayGame(g, g_temp)
    g = plays.play_game()

def auto_play():
    global play
    play = play * -1
    keep_playing()


def keep_playing():
    global play
    if play > 0:
        next_loop()


def insert_tile():
    global g
    global entry
    give = entry.get()
    give_life = give.split()
    ans_length = len(give_life)
    if ans_length == 2:
        try:
            x = int(give_life[0])
            try:
                y = int(give_life[1])
                if 0 < x < N + 1 and 0 < y < N + 1:
                    g[x - 1, y - 1] = 1
            except ValueError:
                print("Integers must be between 1-10!")
        except ValueError:
            print("Integers must be between 1-10!")


class GameOfLife:
    global entry
    rects = []
    grid = []
    pg.init()
    SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pg.time.Clock()
    SCREEN.fill(DEAD)
    blockSize = 20
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT - 100, blockSize):
            rect = pg.Rect(x, y, blockSize, blockSize)
            pg.draw.rect(SCREEN, (0, 0, 0, 0), rect, 1)
            rects.append(rect)

    widthBlocks = int(WIDTH/blockSize)
    heightBlocks = int((HEIGHT-100) / blockSize)

    for i in range(widthBlocks):
        grid.append([])

    for i in range(len(rects)):
        grid[i % heightBlocks].append(rects[i])

    pg.draw.rect(SCREEN, (ALIVE), grid[1][1], 20)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

        pg.display.update()

