import numpy as np
from NeighborhoodScript import NeighborhoodScript

g = np.zeros((10, 10), dtype=int)
g_temp = np.zeros((10, 10), dtype=int)


class PlayGame:

    def __init__(self, game, game_temp):
        self.g = game
        self.g_temp = game_temp

    def play_game(self):
        repeat = input("Number of Iterations for the Game of Life: ")  # number of lifecycles
        repeat_int = int(repeat)
        for i in range(repeat_int):
            self.change_board()
            for x in range(10):
                for y in range(10):
                    self.g[x, y] = self.g_temp[x, y]  # copies g_temp over to g
            print("")
            print(self.g)

    def change_board(self):
        neighbor = NeighborhoodScript(self.g)
        for x in range(10):
            for y in range(10):
                if self.g[x, y] == 0:  # case for when square is dead
                    game = neighbor.neighbors(x, y)
                    if game == 3:
                        self.g_temp[x, y] = 1
                if self.g[x, y] == 1:
                    game = neighbor.neighbors(x, y)
                    if game < 2:  # case for when square is alive
                        self.g_temp[x, y] = 0
                    elif game == 2 or game == 3:
                        self.g_temp[x, y] = 1
                    elif game > 3:
                        self.g_temp[x, y] = 0
                    else:  # should NEVER occur. Error statement in case something goes wrong
                        print("ERROR Something went wrong in life! R.I.P.")
