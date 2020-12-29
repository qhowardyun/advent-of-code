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
            # vertical portal
            if r + 1 < h and grid[r + 1][c].isupper():
                label = char + grid[r + 1][c]
                # entrance below label
                if r + 2 < h and grid[r + 2][c] == ".":
                    portals[label].append(((r + 1, c),(r + 2, c)))
                # entrance above label
                else:
                    portals[label].append(((r, c),(r - 1, c)))

            # horizontal portal
            if c + 1 < w and grid[r][c + 1].isupper():
                label = char + grid[r][c + 1]
                # entrance right of label
                if c + 2 < w and grid[r][c + 2] == ".":
                    portals[label].append(((r, c + 1),(r, c + 2)))
                # entrance left of label
                else:
                    portals[label].append(((r, c),(r, c - 1)))

# get entrance and exit
start = portals.pop("AA")[0][1]
end = portals.pop("ZZ")[0][1]

# setup lookup table
transporter = {}
for v in portals.values():
    transporter[v[0][0]] = v[1][1]
    transporter[v[1][0]] = v[0][1]

dp = {start: 0}
q = deque([start])

while q:
    key = q.popleft()
    curR, curC = key
    cost = dp[key] + 1
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newR = curR + dr
        newC = curC + dc
        char = grid[newR][newC]
        if char == "#":
            continue
        newKey = (newR, newC)
        if char.isupper():
            if newKey not in transporter:
                continue
            newR, newC = transporter[newKey]
        newKey = (newR, newC)

        if (newR, newC) not in dp or dp[newKey] > cost:
            dp[newKey] = cost
            q.append(newKey)
print(dp[end])

