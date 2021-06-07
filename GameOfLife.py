#About: Simple Python implementation of John Conway's Game of Life. So far, the game is limited to a 10x10 grid.
#Rules of the Game
#0 -> dead, 1 -> Alive, neighbor-> alive residents of any of the eight squares surrounding it
#If an alive square have 0-1 neighbors, it dies
#If an alive square have 2-3 neighbors, it lives
#If an alive square have 4 or more neighbors, it dies
#If a dead square have exactly 3 neighbors, it lives
import numpy as np
import time

g = np.zeros((10,10), dtype=int)
g_temp = np.zeros((10,10), dtype=int)
kill = 'y'

def check(x,y): #general case
    count = 0
    if g[x-1,y-1] == 1:#top-left
        count += 1
    if g[x-1,y] == 1: #top
        count += 1
    if g[x,y-1] == 1: #left
        count += 1
    if g[x+1,y+1] == 1: #bottom-right
        count += 1
    if g[x+1,y] == 1: #bottom
        count += 1
    if g[x,y+1] == 1: #right
        count += 1
    if g[x-1,y+1] == 1: #top-right
        count += 1
    if g[x+1,y-1] == 1: #bottom-left
        count += 1
    return count

def check_00(x,y): #case for upper left corner
    count = 0
    if g[x+1,y+1] == 1: #bottom-right
        count += 1
    if g[x+1,y] == 1: #bottom
        count += 1
    if g[x,y+1] == 1: #right
        count += 1
    return count

def check_10(x,y): #case for upper right corner
    count = 0
    if g[x+1,y] == 1: #bottom
        count += 1
    if g[x,y-1] == 1: #left
        count += 1
    if g[x+1,y-1] == 1: #bottom-left
        count += 1
    return count

def check_01(x,y): #case for bottom left corner
    count = 0
    if g[x,y+1] == 1: #right
        count += 1
    if g[x-1,y+1] == 1: #top-right
        count += 1
    if g[x-1,y] == 1: #top
        count += 1
    return count

def check_11(x,y): #case for bottom right corner
    count = 0
    if g[x-1,y-1] == 1:#top-left
        count += 1
    if g[x-1,y] == 1: #top
        count += 1
    if g[x,y-1] == 1: #left
        count += 1
    return count

def check_x0(x,y): #case for top edge
    count = 0
    corner_count = check_00(x,y)
    count += corner_count
    if g[x,y-1] == 1: #left
        count += 1
    if g[x+1,y-1] == 1: #bottom-left
        count += 1
    return count

def check_0y(x,y): #case for left edge
    count = 0
    corner_count = check_00(x,y)
    count += corner_count
    if g[x-1,y] == 1: #top
        count += 1
    if g[x-1,y+1] == 1: #top-right
        count += 1
    return count

def check_x1(x,y): #case for bottom edge
    count = 0
    corner_count = check_11(x,y)
    count += corner_count
    if g[x-1,y+1] == 1: #top-right
        count += 1
    if g[x,y+1] == 1: #right
        count += 1
    return count

def check_1y(x,y): #case for right edge
    count = 0
    corner_count = check_11(x,y)
    count += corner_count
    if g[x+1,y] == 1: #bottom
        count += 1
    if g[x+1,y-1] == 1: #bottom-left
        count += 1
    return count


def neighbors(x,y): #check to see if nearby squares have life, return number of squares with life
    count = 0
    if x==0 and y==0:
        count+=check_00(x,y)
    elif x==0 and y==9:
        count+=check_10(x,y)
    elif x==9 and y==0:
        count+=check_01(x,y)
    elif x==9 and y==9:
        count+=check_11(x,y)
    elif x==0:
        count+=check_x0(x,y)
    elif x==9:
        count+=check_x1(x,y)
    elif y==0:
        count+=check_0y(x,y)
    elif y==9:
        count+=check_1y(x,y)
    else:
        count+=check(x,y)
    return count

game=0

for x in range(10): #copies over g to g_temp
    for y in range(10):
        g_temp[x,y]=g[x,y]


while kill=="y":#repeats game if user does not quit
    print(g)
    print("")
    q = "y"  # stops loops for coordinates if answer is not y
    while q=="y": #ask for coordinates, must be in the form +int +int. Other froms will be rejected
        ans = input("Enter coordinates for where life should be (ex: 2 2): ")
        ans_array = ans.split()
        ans_length =len(ans_array)
        if(ans_length == 2):
            try:
                x = int(ans_array[0])
                try:
                    y = int(ans_array[1])
                    if(x>0 and y>0 and x<11 and y<11):
                        g[x,y] = 1
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
    repeat = input("Number of Iterations for the Game of Life: ") #number of lifecycles
    repeat_int = int(repeat)
    for i in range(repeat_int):
        for x in range(10):
            for y in range(10):
                if g[x,y]==0: #case for when square is dead
                    game = neighbors(x,y)
                    if game==3:
                        g_temp[x,y]=1;
                if g[x,y]==1:
                    game = neighbors(x,y)
                    if game<2: #case for when square is alive
                        g_temp[x,y]=0
                    elif game==2 or game==3:
                        g_temp[x,y]=1
                    elif game>3:
                        g_temp[x,y]=0
                    else: #should NEVER occur. Error statement in case something goes wrong
                        print("ERROR Something went wrong in life! R.I.P.")
        for x in range(10):
            for y in range(10):
                g[x, y] = g_temp[x, y] #copies g_temp over to g
        print("")
        print(g)
    kill = "w"
    while kill != "n" and kill != "y": #determines if user will quit the game or not
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
    #for x in range(10):
        #for y in range(10):
    #neighbors(1,2);