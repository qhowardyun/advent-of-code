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
    row.insert(0, '.')
    row.append('.')
grid.insert(0, ['.'] * (len(data[0]) + 2))
grid.append(['.'] * (len(data[0]) + 2))


def count(r, c):
    xm = [-1, 0, 1, -1, 1, -1, 0, 1]
    ym = [-1, -1, -1, 0, 0, 1, 1, 1]

    count = 0
    for cx, cy in zip(xm, ym):
        # print(grid[r + cy][c + cx])
        if grid[r + cy][c + cx] == "#":
            count += 1
    return count

newgrid = []

while True:
    print("\n".join(["".join(line) for line in newgrid]))
    print()
    newgrid = copy.deepcopy(grid)
    for r in range(1, len(data) + 1):
        for c in range(1, w + 1):
            cnt = count(r, c)
            if grid[r][c] == "L" and cnt == 0:
                newgrid[r][c] = "#"
            elif grid[r][c] == "#" and cnt >= 4:
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
