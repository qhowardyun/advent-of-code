import math
import itertools
from aocd import get_data, submit
from copy import deepcopy

data = get_data(day=17, year=2020)
# data = """.#.
# ..#
# ###"""
lines = data.splitlines()

SIZE = 50

grid = [[[False for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]


for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == "#":
            m = int(SIZE / 2)
            grid[m + x][m + y][m] = True

for _ in range(6):
    gridcopy = deepcopy(grid)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            for z in range(len(grid[x][y])):

                nei = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        for dz in [-1, 0, 1]:
                            if dx == 0 and dy == 0 and dz == 0:
                                continue

                            cx = x + dx
                            cy = y + dy
                            cz = z + dz

                            if 0 <= cx < SIZE and 0 <= cy < SIZE and 0 <= cz < SIZE:
                                if grid[cx][cy][cz]:
                                    # print("found", cx, cy, cz)
                                    nei += 1

                if grid[x][y][z] and (nei == 2 or nei ==3):
                    gridcopy[x][y][z] = True
                else:
                    gridcopy[x][y][z] = False

                if not grid[x][y][z] and nei == 3:
                    gridcopy[x][y][z] = True

    grid = deepcopy(gridcopy)


total = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        for z in range(len(grid[x][y])):
            if grid[x][y][z]:
                total += 1

print(total)

