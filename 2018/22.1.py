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

padding = 50

tc += 1
tr += 1

grid = [[0 for _ in range(tc + padding)] for _ in range(tr + padding)]

for r in range(tr + padding):
    grid[r][0] = ((r * 48271 + depth) % 20183)

for c in range(tc + padding):
    grid[0][c] = ((c * 16807 + depth) % 20183)

grid[0][0] = (0 + depth) % 20183

for r in range(1, tr + padding):
    for c in range(1, tc + padding):
        grid[r][c] = (grid[r-1][c] * grid[r][c-1] + depth) % 20183

grid[tr - 1][tc - 1] = (0 + depth) % 20183

# s = [".","=", "|"]
# print("\n".join(["".join([s[c % 3] for c in row]) for row in grid]))

MAX = 10 ** 10
TORCH = 0
GEAR = 1
NEITHER = 2

ROCKY = 0
WET = 1
NARROW = 2

dp = [[[MAX, MAX, MAX] for _ in range(tc + padding)] for _ in range(tr + padding)]
dp[0][0][0] = 0
q = set([(0,0,0)])

def addValue(ir, ic, destTool, srcTool, v):
    # time to switch tools
    if destTool != srcTool:
        v += 7
    # time between regions
    v += 1

    if v < dp[ir][ic][destTool]:
        dp[ir][ic][destTool] = v
        q.add((ir, ic, destTool))

while q:
    r, c, srctyp = q.pop()
    for dr, dc, bt in [(0, 1, "<"), (1, 0, "^"), (0, -1, ">"), (-1, 0, "v")]:
        nr = r + dr
        nc = c + dc

        # avoid out of bounds
        if nr >= tr + padding  or nr < 0 or nc >= tc + padding or nc < 0:
            continue

        srcv = dp[r][c][srctyp]
        sourceGeo = grid[r][c] % 3
        destGeo = grid[nr][nc] % 3

        if destGeo == ROCKY:
            if sourceGeo == ROCKY or sourceGeo == NARROW:
                addValue(nr, nc, TORCH, srctyp, srcv)
            if sourceGeo == ROCKY or sourceGeo == WET:
                addValue(nr, nc, GEAR, srctyp, srcv)
        elif destGeo == WET:
            if sourceGeo == ROCKY or sourceGeo == WET:
                addValue(nr, nc, GEAR, srctyp, srcv)
            if sourceGeo == WET or sourceGeo == NARROW:
                addValue(nr, nc, NEITHER, srctyp, srcv)
        elif destGeo == NARROW:
            if sourceGeo == WET or sourceGeo == NARROW:
                addValue(nr, nc, NEITHER, srctyp, srcv)
            if sourceGeo == ROCKY or sourceGeo == NARROW:
                addValue(nr, nc, TORCH, srctyp, srcv)

torch = dp[tr-1][tc-1][0]
gear = dp[tr-1][tc-1][1] + 7
print(min(torch, gear))
