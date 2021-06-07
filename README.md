# Game-of-Life
A 10x10 grid that plays John Conway's Game of Life. The grid is implemented via a Numpy 2darray.
Players can dictate which squares on the grid they want to have life. The rules of the game are simple.

1 = life. 0 = dead. Neighbor = Any life surrounding a square.

Rules:
If a square that has life is underpopulated (it has 0-1 neighbors), it dies on the next turn.
If a square that has life is safely populated (it has 2-3 neighbors), it lives onto the next turn.
If a square that has life is overpopulated (it has 4 or more neighbors), it dies the next turn.
If a square that is dead can be repopulated with life it has exactly 3 neighbors.

# How to Run
Run the GameOfLife.py script located under the Game-of-Life directory.
