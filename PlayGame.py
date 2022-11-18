import numpy as np
from NeighborhoodScript import NeighborhoodScript

N = int((1080-100)/20)
M = int(1940/20)
g = np.zeros((N, N), dtype=int)
g_temp = np.zeros((N, N), dtype=int)


class PlayGame:

    def __init__(self, game, game_temp):
        self.g = game
        self.g_temp = game_temp

    def play_game(self):
        self.change_board()
        for x in range(N):
            for y in range(M-1):
                self.g[x, y] = self.g_temp[x, y]  # copies g_temp over to g
        return self.g

    def change_board(self):
        neighbor = NeighborhoodScript(self.g)
        for x in range(N):
            for y in range(M-1):
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
