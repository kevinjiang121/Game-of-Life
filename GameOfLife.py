# About: Simple Python implementation of John Conway's Game of Life. So far, the game is limited to a 10x10 grid.
# Rules of the Game
# 0 -> dead, 1 -> Alive, neighbor-> alive residents of any of the eight squares surrounding it
# If an alive square have 0-1 neighbors, it dies
# If an alive square have 2-3 neighbors, it lives
# If an alive square have 4 or more neighbors, it dies
# If a dead square have exactly 3 neighbors, it lives
import numpy as np
from NeighborhoodScript import NeighborhoodScript
from SetGame import SetGame

g = np.zeros((10, 10), dtype=int)
g_temp = np.zeros((10, 10), dtype=int)
kill = 'y'

while kill == "y":  # repeats game if user does not quit
    game = SetGame()
    g = game.createBoard()
    repeat = input("Number of Iterations for the Game of Life: ")  # number of lifecycles
    repeat_int = int(repeat)
    for i in range(repeat_int):
        neighbor = NeighborhoodScript(g)
        for x in range(10):
            for y in range(10):
                if g[x, y] == 0:  # case for when square is dead
                    game = neighbor.neighbors(x, y)
                    if game == 3:
                        g_temp[x, y] = 1
                if g[x, y] == 1:
                    game = neighbor.neighbors(x, y)
                    if game < 2:  # case for when square is alive
                        g_temp[x, y] = 0
                    elif game == 2 or game == 3:
                        g_temp[x, y] = 1
                    elif game > 3:
                        g_temp[x, y] = 0
                    else:  # should NEVER occur. Error statement in case something goes wrong
                        print("ERROR Something went wrong in life! R.I.P.")
        for x in range(10):
            for y in range(10):
                g[x, y] = g_temp[x, y]  # copies g_temp over to g
        print("")
        print(g)
    kill = "w"
    while kill != "n" and kill != "y":  # determines if user will quit the game or not
        kill = input("Continue? (y/n): ")
        if kill == "y":
            print("")
            print("Starting new game...")
            for x in range(10):
                for y in range(10):
                    g[x, y] = 0
                    g_temp[x, y] = 0
        elif kill == "n":
            print("")
            print("Quitting program...")
        else:
            print("Please enter valid input (y-yes, n-no): ")
            print("")
