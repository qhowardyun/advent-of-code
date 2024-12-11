from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

day = 6
data = get_data(day=day, year=2024)
grid = data.splitlines()

ans = 0

gr, gc = 0, 0

for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == "^":
            gr, gc = r, c
            break

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cdir = 0

print(gr, gc)

visited = set()
visited.add((gc, gr))

while True:
    nr = gr + dir[cdir % 4][0]
    nc = gc + dir[cdir % 4][1]

    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
        break

    if grid[nr][nc] == "#":
        cdir += 1
    else:
        gr, gc = nr, nc
        visited.add((gc, gr))




ans = len(visited)


print(visited)




print(ans)

assert ans != 0
submit(ans, part="a", day=day, year=2024, reopen=False)
# submit(ans, part="b", day=day, year=2024, reopen=False)
