import numpy as np

g = np.zeros((10, 10), dtype=int)

class SetGame:
    def __init__(self):
        pass

    def createBoard(self):
        print(g)
        print("")
        q = "y"  # stops loops for coordinates if answer is not y
        while q == "y":  # ask for coordinates, must be in the form +int +int. Other forms will be rejected
            ans = input("Enter coordinates for where life should be (ex: 2 2): ")
            ans_array = ans.split()
            ans_length = len(ans_array)
            if ans_length == 2:
                try:
                    x = int(ans_array[0])
                    try:
                        y = int(ans_array[1])
                        if 0 < x < 11 and 0 < y < 11:
                            g[x, y] = 1
                            print(g)
                            print("")
                            q = input("Do you want enter another coordinate (y/n): ")
                    except ValueError:
                        print("Integers must be between 1-10!")
                except ValueError:
                    print("Integers must be between 1-10!")
            else:
                print("Only 2 coordinates are allowed. Please try again.")
        print("")
        return g