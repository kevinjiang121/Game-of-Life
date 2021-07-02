# About: Simple Python implementation of John Conway's Game of Life. So far, the game is limited to a 10x10 grid.
# Rules of the Game
# 0 -> dead, 1 -> Alive, neighbor-> alive residents of any of the eight squares surrounding it
# If an alive square have 0-1 neighbors, it dies
# If an alive square have 2-3 neighbors, it lives
# If an alive square have 4 or more neighbors, it dies
# If a dead square have exactly 3 neighbors, it lives

import numpy as np
import tkinter as tk
from time import *
from PlayGame import PlayGame

g = np.zeros((10, 10), dtype=int)
g_temp = np.zeros((10, 10), dtype=int)

root = tk.Tk()
root.title('Game of Life')
entry = tk.Entry()
play = -1


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
    plays = PlayGame(g, g_temp)
    g = plays.play_game()
    display_game()


def display_game():
    for r in range(10):
        for c in range(10):
            if g[r, c] == 1:
                tile = tk.Canvas(root, height=50, width=50, bg="black")
            else:
                tile = tk.Canvas(root, height=50, width=50, bg="white")
            tile.grid(row=r, column=c)


def auto_play():
    global play
    play = play * -1
    keep_playing()

def keep_playing():
    global play
    if play>0:
        next_loop()
        root.after(1000, keep_playing)

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
    root.geometry('550x700')
    enter_label = tk.Label(root, text="Please enter a coordinate from 1-10 (ex:2 2)")
    btn = tk.Button(root, text='Next Life Cycle', bd='10', command=next_loop)
    btn_clear = tk.Button(root, text='Clear Board', bd='10', command=clear_board)
    btn_auto = tk.Button(root, text='Auto', bd='10', command=auto_play)
    entry = tk.Entry(root)
    btn_insert = tk.Button(root, text='Insert', bd='10', command=insert_tile)
    display_game()
    btn_auto.place(x=400, y=550)
    btn.place(x=400, y=600)
    btn_clear.place(x=400, y=650)
    enter_label.place(x=85, y=565)
    entry.place(x=100, y=600)
    btn_insert.place(x=230, y=585)
    root.mainloop()
