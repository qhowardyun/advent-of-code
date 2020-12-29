from aocd import get_data
from collections import defaultdict, deque

data = get_data(day=20, year=2019)

grid = list(map(list, data.splitlines()))
w = len(grid[0])
h = len(grid)

portals = defaultdict(list)

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char.isupper():
            label = ""
            inc = ""
            outc = ""
            isOuter = (r < 5) or (r + 5 > h) or (c < 5) or (c + 5 > w)
            # vertical portal
            if r + 1 < h and grid[r + 1][c].isupper():
                label = char + grid[r + 1][c]
                # entrance below label
                if r + 2 < h and grid[r + 2][c] == ".":
                    inc = (r + 1, c)
                    outc = (r + 2, c)
                # entrance above label
                else:
                    inc = (r, c)
                    outc = (r - 1, c)

            # horizontal portal
            if c + 1 < w and grid[r][c + 1].isupper():
                label = char + grid[r][c + 1]
                # entrance right of label
                if c + 2 < w and grid[r][c + 2] == ".":
                    inc = (r, c + 1)
                    outc = (r, c + 2)
                # entrance left of label
                else:
                    inc = (r, c)
                    outc = (r, c - 1)
            if label:
                portals[label].append((inc, outc, 1 if isOuter else -1))

# get entrance and exit
startR, startC = portals.pop("AA")[0][1]
endR, endC = portals.pop("ZZ")[0][1]

# setup lookup table
transporter = {}
for v in portals.values():
    transporter[v[0][0]] = (v[1][1], v[1][2])
    transporter[v[1][0]] = (v[0][1], v[0][2])

startKey = (startR, startC, 0)
dp = {startKey: 0}
q = deque([startKey])

while q:
    key = q.popleft()
    curR, curC, depth = key
    cost = dp[key] + 1

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newR = curR + dr
        newC = curC + dc
        char = grid[newR][newC]
        if char == "#":
            continue
        newKey = (newR, newC)
        newDepth = depth
        if char.isupper():
            if newKey not in transporter:
                continue
            (newR, newC), depthChange = transporter[newKey]
            newDepth += depthChange

            if newDepth < 0 or newDepth > 100:
                continue
        newKey = (newR, newC, newDepth)
        if newKey not in dp or dp[newKey] > cost:
            dp[newKey] = cost
            q.append(newKey)

print(dp[(endR, endC, 0)])
