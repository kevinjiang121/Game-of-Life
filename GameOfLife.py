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
import math
import numpy as np
from PlayGame import PlayGame
import pygame as pg

N = int((1080 - 100) / 20)
M = int(1940 / 20)
ALIVE = (0, 0, 0)
DEAD = (255, 255, 255)
HEIGHT = 1080
WIDTH = 1940

g = np.zeros((N, M), dtype=int)
g_temp = np.zeros((N, M), dtype=int)

play = -1


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


class GameOfLife:
    pg.init()
    pg.font.init()
    font = pg.font.SysFont('Times New Roman', 75)
    nextTurn = font.render('Next Round', False, (0, 0, 0))

    rects = []
    grid = []
    rectPos = [0, 0]
    SCREEN = pg.display.set_mode((WIDTH - 20, HEIGHT))
    CLOCK = pg.time.Clock()
    SCREEN.fill(DEAD)
    blockSize = 20
    clear = pg.Rect(0, HEIGHT - 100, 660, 100)
    next = pg.Rect(660, HEIGHT - 100, 660, 100)
    auto = pg.Rect(1320, HEIGHT - 100, 660, 100)
    pg.draw.rect(SCREEN, (0, 0, 0, 0), clear, 3)
    pg.draw.rect(SCREEN, (0, 0, 0, 0), next, 3)
    pg.draw.rect(SCREEN, (0, 0, 0, 0), auto, 3)
    SCREEN.blit(nextTurn, (800, HEIGHT - 100))

    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT - 100, blockSize):
            rect = pg.Rect(x, y, blockSize, blockSize)
            pg.draw.rect(SCREEN, (0, 0, 0, 0), rect, 1)
            rects.append(rect)

    widthBlocks = int(WIDTH / blockSize)
    heightBlocks = int((HEIGHT - 100) / blockSize)

    for i in range(widthBlocks):
        grid.append([])

    for i in range(len(rects)):
        grid[i % heightBlocks].append(rects[i])

    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                rectPos = pg.mouse.get_pos()

            if rectPos[1] < HEIGHT - 100:
                if event.type == pg.MOUSEBUTTONUP:
                    pg.draw.rect(SCREEN, ALIVE, grid[math.floor(rectPos[1] / 20)][math.floor(rectPos[0] / 20)], 20)
                    g[math.floor(rectPos[1] / 20)][math.floor(rectPos[0] / 20)] = 1

            if rectPos[1] > HEIGHT - 100 and rectPos[0] < 660:
                '''
                if event.type == pg.MOUSEBUTTONUP:
                    SCREEN.fill(DEAD)
                    for i in range(len(rects)):
                        pg.draw.rect(SCREEN, ALIVE, rects[i], 1)
                    pg.draw.rect(SCREEN, ALIVE, clear, 3)
                    pg.draw.rect(SCREEN, ALIVE, next, 3)
                    pg.draw.rect(SCREEN, ALIVE, auto, 3)
                    g = np.zeros((N, M), dtype=int)
                '''
            if rectPos[1] > HEIGHT - 100 and 660 < rectPos[0] <= 1320:
                if event.type == pg.MOUSEBUTTONUP:
                    next_loop()
                    for i in range(len(g)):
                        for j in range(len(g[i])):
                            if g[i][j] == 1:
                                pg.draw.rect(SCREEN, DEAD, grid[i][j], 20)
                                pg.draw.rect(SCREEN, ALIVE, grid[i][j], 20)
                            if g[i][j] == 0:
                                pg.draw.rect(SCREEN, DEAD, grid[i][j], 20)
                                pg.draw.rect(SCREEN, ALIVE, grid[i][j], 1)
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

        pg.display.update()
