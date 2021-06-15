# About: Simple Python implementation of John Conway's Game of Life. So far, the game is limited to a 10x10 grid.
# Rules of the Game
# 0 -> dead, 1 -> Alive, neighbor-> alive residents of any of the eight squares surrounding it
# If an alive square have 0-1 neighbors, it dies
# If an alive square have 2-3 neighbors, it lives
# If an alive square have 4 or more neighbors, it dies
# If a dead square have exactly 3 neighbors, it lives
import numpy as np
from SetGame import SetGame
from PlayGame import PlayGame

g = np.zeros((10, 10), dtype=int)
g_temp = np.zeros((10, 10), dtype=int)
kill = 'y'


def clear_board():
    for x in range(10):
        for y in range(10):
            g[x, y] = 0
            g_temp[x, y] = 0


def continue_game():
    kill_game = "w"
    while kill_game != "n" and kill_game != "y":  # determines if user will quit the game or not
        print("")
        kill_game = input("Continue? (y/n): ")
        if kill_game == "y":
            print("")
            print("Starting new game...")
        elif kill_game == "n":
            print("")
            print("Quitting program...")
        else:
            print("Please enter valid input (y-yes, n-no): ")
            print("")
    return kill_game


class GameOfLife:
    while kill == "y":  # repeats game if user does not quit
        clear_board()
        game = SetGame()
        g = game.createBoard()
        play = PlayGame(g, g_temp)
        play.play_game()
        kill = continue_game()
