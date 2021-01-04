from copy import deepcopy
from aocd import get_data

data = get_data(day=24, year=2019)

lines = data.splitlines()

grid = [list(line) for line in lines]


SEEN = set()

while True:
    gridcopy = deepcopy(grid)

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            count = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newr = r + dr
                newc = c + dc
                if 0 <= newr < 5 and 0 <= newc < 5:
                    if gridcopy[newr][newc] == "#":
                        count += 1

            if char == "#" and count != 1:
                grid[r][c] = "."
            elif char == "." and (count == 1 or count == 2):
                grid[r][c] = "#"

    score = 0
    value = 1
    for row in grid:
        for char in row:
            if char == "#":
                score += value
            value *= 2
    if score in SEEN:
        print(score)
        exit()
    else:
        SEEN.add(score)
