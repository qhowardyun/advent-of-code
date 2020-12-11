import math
import itertools
import functools
import copy
from aocd import get_data, submit

data = get_data(day=11, year=2020)
data = data.splitlines()

w = len(data[0])

grid = []
for row in data:
    grid.append(list(row))
for row in grid:
    row.insert(0, '|')
    row.append('|')
grid.insert(0, ['|'] * (len(data[0]) + 2))
grid.append(['|'] * (len(data[0]) + 2))


def count(r, c):

    rm = [-1, -1, -1, 0, 0, 1, 1, 1]
    cm = [-1, 0, 1, -1, 1, -1, 0, 1]

    count = 0
    for rc, cc in zip(rm, cm):
        curr = r
        curc = c
        while True:
            curr += rc
            curc += cc

            if (grid[curr][curc] == "|"):
                break
            if (grid[curr][curc] == "L"):
                break
            if (grid[curr][curc] == "#"):
                count += 1
                break
    return count

newgrid = []

while True:
    # input()
    print("\n".join(["".join(line) for line in grid]))
    print()
    newgrid = copy.deepcopy(grid)
    for r in range(1, len(data) + 1):
        for c in range(1, w + 1):
            cnt = count(r, c)
            if grid[r][c] == "L" and cnt == 0:
                newgrid[r][c] = "#"
            elif grid[r][c] == "#" and cnt >= 5:
                newgrid[r][c] = "L"
    if newgrid == grid:
        break
    else:
        grid = copy.deepcopy(newgrid)
total = 0

for line in grid:
    for c in line:
        if c == "#":
            total += 1

print(total)
