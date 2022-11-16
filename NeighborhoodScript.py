import numpy as np

N = 100
g = np.zeros((N, N), dtype=int)


class NeighborhoodScript:

    def __init__(self, game):
        self.g = game

    def neighbors(self, x, y):  # check to see if nearby squares have life, return number of squares with life
        count = 0
        if x == 0 and y == 0:
            count += self.check_00(x, y)
        elif x == 0 and y == N - 1:
            count += self.check_10(x, y)
        elif x == N - 1 and y == 0:
            count += self.check_01(x, y)
        elif x == N - 1 and y == N - 1:
            count += self.check_11(x, y)
        elif x == 0:
            count += self.check_x0(x, y)
        elif x == N - 1:
            count += self.check_x1(x, y)
        elif y == 0:
            count += self.check_0y(x, y)
        elif y == N - 1:
            count += self.check_1y(x, y)
        else:
            count += self.check(x, y)
        return count

    def check(self, x, y):  # general case
        count = 0
        if self.g[x - 1, y - 1] == 1:  # top-left
            count += 1
        if self.g[x - 1, y] == 1:  # top
            count += 1
        if self.g[x, y - 1] == 1:  # left
            count += 1
        if self.g[x + 1, y + 1] == 1:  # bottom-right
            count += 1
        if self.g[x + 1, y] == 1:  # bottom
            count += 1
        if self.g[x, y + 1] == 1:  # right
            count += 1
        if self.g[x - 1, y + 1] == 1:  # top-right
            count += 1
        if self.g[x + 1, y - 1] == 1:  # bottom-left
            count += 1
        return count

    def check_00(self, x, y):  # case for upper left corner
        count = 0
        if self.g[x + 1, y + 1] == 1:  # bottom-right
            count += 1
        if self.g[x + 1, y] == 1:  # bottom
            count += 1
        if self.g[x, y + 1] == 1:  # right
            count += 1
        return count

    def check_10(self, x, y):  # case for upper right corner
        count = 0
        if self.g[x + 1, y] == 1:  # bottom
            count += 1
        if self.g[x, y - 1] == 1:  # left
            count += 1
        if self.g[x + 1, y - 1] == 1:  # bottom-left
            count += 1
        return count

    def check_01(self, x, y):  # case for bottom left corner
        count = 0
        if self.g[x, y + 1] == 1:  # right
            count += 1
        if self.g[x - 1, y + 1] == 1:  # top-right
            count += 1
        if self.g[x - 1, y] == 1:  # top
            count += 1
        return count

    def check_11(self, x, y):  # case for bottom right corner
        count = 0
        if self.g[x - 1, y - 1] == 1:  # top-left
            count += 1
        if self.g[x - 1, y] == 1:  # top
            count += 1
        if self.g[x, y - 1] == 1:  # left
            count += 1
        return count

    def check_x0(self, x, y):  # case for top edge
        count = 0
        corner_count = self.check_00(x, y)
        count += corner_count
        if self.g[x, y - 1] == 1:  # left
            count += 1
        if self.g[x + 1, y - 1] == 1:  # bottom-left
            count += 1
        return count

    def check_0y(self, x, y):  # case for left edge
        count = 0
        corner_count = self.check_00(x, y)
        count += corner_count
        if self.g[x - 1, y] == 1:  # top
            count += 1
        if self.g[x - 1, y + 1] == 1:  # top-right
            count += 1
        return count

    def check_x1(self, x, y):  # case for bottom edge
        count = 0
        corner_count = self.check_11(x, y)
        count += corner_count
        if self.g[x - 1, y + 1] == 1:  # top-right
            count += 1
        if self.g[x, y + 1] == 1:  # right
            count += 1
        return count

    def check_1y(self, x, y):  # case for right edge
        count = 0
        corner_count = self.check_11(x, y)
        count += corner_count
        if self.g[x + 1, y] == 1:  # bottom
            count += 1
        if self.g[x + 1, y - 1] == 1:  # bottom-left
            count += 1
        return count
