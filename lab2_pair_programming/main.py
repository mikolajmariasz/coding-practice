import random
import os
from time import sleep

WIDTH = 40
HEIGHT = 20
DELAY = 1.0

grid = []
for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
        if random.random() < 0.5:
            row.append(1)
        else:
            row.append(0)
    grid.append(row)


while True:
    os.system('cls')
    for i in range(HEIGHT):
        print("\n", end="")
        for j in range(WIDTH):
            if grid[i][j] == 1:
                print("O", end=" ")
            else:
                print(".", end=" ")

    new_grid = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(0)
        new_grid.append(row)

    for x in range(HEIGHT):
        for y in range(WIDTH):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    nx = (x + i) % HEIGHT
                    ny = (y + j) % WIDTH
                    neighbors += grid[nx][ny]
            if grid[x][y] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0

    grid = new_grid

    sleep(DELAY)