import numpy as np
import pygame as pg

N = int((1080 - 100) / 20)
M = int(1940 / 20)
g = np.zeros((N, M), dtype=int)
HEIGHT = 1080
WIDTH = 1940
ALIVE = (0, 0, 0)
DEAD = (255, 255, 255)


class SetGame:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Game of Life')
        pg.font.init()

    def render_window(self):
        font = pg.font.SysFont('Times New Roman', 75)
        nextTurn = font.render('Next Round', False, (0, 0, 0))
        autoText = font.render('Auto', False, (0, 0, 0))
        clearText = font.render('Clear Board', False, (0, 0, 0))

        rects = []
        grid = []
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
        SCREEN.blit(clearText, (150, HEIGHT - 100))
        SCREEN.blit(nextTurn, (800, HEIGHT - 100))
        SCREEN.blit(autoText, (1550, HEIGHT - 100))

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

        return grid, rects, SCREEN

    def create_board(self):
        return self.render_window()
