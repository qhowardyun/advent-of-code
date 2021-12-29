from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 20
ans = 0
data = get_data(day=day, year=2021)

lookup, gridt = data.split("\n\n")
gridl = gridt.splitlines()


grid = [["." for _ in range(len(gridl[0]) + 110)] for _ in range(55)]

for line in gridl:
    grid.append(["."] * 55 + list(line) + ["."] * 55)

for _ in range(55):
    grid.append(["." for _ in range(len(gridl[0]) + 110)])


state = "#"

for _ in range(50):

    state = "." if state == "#" else "#"

    ngrid = [["" for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            val = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    val *= 2
                    lr = r + dr
                    lc = c + dc
                    val += (
                        1
                        if (
                            grid[lr][lc]
                            if 0 <= lr < len(grid) and 0 <= lc < len(grid[0])
                            else state
                        )
                        == "#"
                        else 0
                    )

            ngrid[r][c] = lookup[val]
    grid = ngrid

ans = 0

for row in grid:
    for c in row:
        if c == "#":
            ans += 1


print(ans)
submit(ans, part="b", day=day, year=2021, reopen=False)
