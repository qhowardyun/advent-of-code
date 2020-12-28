from aocd import get_data

from collections import deque

data = get_data(day=18, year=2019)
grid = data.splitlines()

def printGrid():
    print(*grid, sep="\n")

startr, startc = 0,0
pos = {}

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "@":
            startr = r
            startc = c
        elif char != "#" and char != "." and char.islower():
            pos[char] = (r, c)

q = deque()
q.append((startr, startc, 0))

dp = {}
dp[(startr,startc,0)] = 0

def update(r, c, doors, cost):
    key = (r, c, doors)
    if (key not in dp) or dp[key] > cost:
        # print("found:", r, c, doors, cost)
        dp[(r, c, doors)] = cost
        q.append((r, c, doors))

def isDoorOpen(n, door):
    k = ord(door) - ord("a")
    if n & (1 << k):
        return True
    else:
        return False

def openDoor(n, door):
    k = ord(door) - ord("a")
    return n | (1 << k)

steps = 0

while q:
    steps += 1
    curR, curC, doors = q.popleft()
    cost = dp[(curR, curC, doors)] + 1
    for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        newR = curR + dr
        newC = curC + dc
        char = grid[newR][newC]

        if char == "#":
            continue
        elif char.islower():
            newDoors = openDoor(doors, char.lower())
            update(newR, newC, newDoors, cost)
        elif char.isupper():
            if isDoorOpen(doors, char.lower()):
                update(newR, newC, doors, cost)
        else:
            update(newR, newC, doors, cost)
dmax = 0
costmin = 10 ** 8
for (r, c, doors), v in dp.items():
    if doors == (2 ** len(pos.keys())) - 1:
        costmin = min(costmin, v)
print(costmin)
