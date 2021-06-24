# About: Simple Python implementation of John Conway's Game of Life. So far, the game is limited to a 10x10 grid.
# Rules of the Game
# 0 -> dead, 1 -> Alive, neighbor-> alive residents of any of the eight squares surrounding it
# If an alive square have 0-1 neighbors, it dies
# If an alive square have 2-3 neighbors, it lives
# If an alive square have 4 or more neighbors, it dies
# If a dead square have exactly 3 neighbors, it lives

import numpy as np
import tkinter as tk
from PlayGame import PlayGame

g = np.zeros((10, 10), dtype=int)
g_temp = np.zeros((10, 10), dtype=int)

root = tk.Tk()
entry = tk.Entry()


def clear_board():
    for x in range(10):
        for y in range(10):
            g[x, y] = 0
            g_temp[x, y] = 0
    display_game()


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


def next_loop():
    global g
    play = PlayGame(g, g_temp)
    g = play.play_game()
    display_game()


def display_game():
    for r in range(10):
        for c in range(10):
            if g[r, c] == 1:
                tile = tk.Canvas(root, height=50, width=50, bg="black")
            else:
                tile = tk.Canvas(root, height=50, width=50, bg="white")
            tile.grid(row=r, column=c)


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
                if 0 < x < 11 and 0 < y < 11:
                    g[x - 1, y - 1] = 1
            except ValueError:
                print("Integers must be between 1-10!")
        except ValueError:
            print("Integers must be between 1-10!")
    display_game()


class GameOfLife:
    global entry
    root.geometry('1980x1080')
    enter_label = tk.Label(root, text="Please enter a coordinate from 1-10 (ex:2 2)")
    btn = tk.Button(root, text='Next Life Cycle', bd='10', command=next_loop)
    btn_close = tk.Button(root, text='Close', bd='10', command=root.destroy)
    btn_clear = tk.Button(root, text='Clear Board', bd='10', command=clear_board)
    entry = tk.Entry(root)
    btn_insert = tk.Button(root, text='Insert', bd='10', command=insert_tile)
    display_game()
    btn.grid(row=11, column=12)
    btn_close.grid(row=11, column=13)
    btn_clear.grid(row=11, column=14)
    enter_label.grid(row=12, column=11)
    btn_insert.grid(row=13, column=12)
    entry.grid(row=13, column=11)
    root.mainloop()
