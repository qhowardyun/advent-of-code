import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=22, year=2018)
lines = data.splitlines()

depth = int(lines[0].split()[1])
tc, tr = map(int, lines[1].split()[1].split(","))

# testcase
# depth = 510
# tc, tr = 10, 10

tc += 1
tr += 1

grid = [[0 for _ in range(tc)] for _ in range(tr)]

for r in range(tr):
    grid[r][0] = ((r * 48271 + depth) % 20183)

for c in range(tc):
    grid[0][c] = ((c * 16807 + depth) % 20183)

grid[0][0] = (0 + depth) % 20183

for r in range(1, tr):
    for c in range(1, tc):
        grid[r][c] = (grid[r-1][c] * grid[r][c-1] + depth) % 20183

grid[tr - 1][tc - 1] = (0 + depth) % 20183


s = [".","=", "|"]
print("\n".join(["".join([s[c % 3] for c in row]) for row in grid]))

danger = 0

for r in range(tr):
    for c in range(tc):
        danger += grid[r][c] % 3

print(danger)
