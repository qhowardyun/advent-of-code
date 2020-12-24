from aocd import get_data
from copy import deepcopy

data = get_data(day=24, year=2020)
lines = data.splitlines()
grid = [[True for _ in range(500)] for _ in range(500)]

for line in lines:
    curx, cury = 250, 250
    up = False
    down = False
    dx, dy = 0, 0
    offset = False
    for c in line:
        if up and c == "e":
            if not offset:
                dx += 1
            dy += 1
            up = False
            offset = not offset
        elif up and c == "w":
            if offset:
                dx -= 1
            dy += 1
            up = False
            offset = not offset
        elif down and c == "e":
            if not offset:
                dx += 1
            dy += -1
            down = False
            offset = not offset
        elif down and c == "w":
            if offset:
                dx -= 1
            dy += -1
            down = False
            offset = not offset
        elif c == "s":
            down = True
        elif c == "n":
            up = True
        elif c == "e":
            dx += 1
        elif c == "w":
            dx += -1
        else:
            assert False
    newx, newy = curx + dx, cury + dy
    grid[newx][newy] = not grid[newx][newy]


for day in range(100):
    newgrid = deepcopy(grid)
    for x, row in enumerate(grid[1:-1]):
        for y, val in enumerate(row[1:-1]):
            neib = 0
            # offset
            if y % 2 == 0:
                for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0)]:
                    if not grid[x + dx][y + dy]:
                        neib += 1
            else:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                    if not grid[x + dx][y + dy]:
                        neib += 1
            if not grid[x][y] and (neib == 0 or neib > 2):
                newgrid[x][y] = True
            elif grid[x][y] and neib == 2:
                newgrid[x][y] = False
    grid = deepcopy(newgrid)

total = 0
for row in grid:
    for c in row:
        if not c:
            total += 1
print(total)



