from aocd import get_data

from collections import deque
from functools import lru_cache

data = get_data(day=18, year=2019)
# data = """#######
# #a.#Cd#
# ##...##
# ##.@.##
# ##...##
# #cB#Ab#
# #######"""

# data = """###############
# #d.ABC.#.....a#
# ######...######
# ######.@.######
# ######...######
# #b.....#.....c#
# ###############"""

# data = """#############
# #DcBa.#.GhKl#
# #.###...#I###
# #e#d#.@.#j#k#
# ###C#...###J#
# #fEbA.#.FgHi#
# #############"""

# data = """#############
# #g#f.D#..h#l#
# #F###e#E###.#
# #dCba...BcIJ#
# #####.@.#####
# #nK.L...G...#
# #M###N#H###.#
# #o#m..#i#jk.#
# #############"""

def printGrid():
    print(*grid, sep="\n")

grid = data.splitlines()
startr, startc = 0,0
pos = {}

# find starting position
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "@":
            startr = r
            startc = c
        elif char != "#" and char != "." and char.islower():
            pos[char] = (r, c)

ALL_DOORS = 2 ** len(pos) - 1

# edit map
grid = [list(row) for row in grid]
grid[startr - 1][startc - 1] = "1"
grid[startr - 1][startc]     = "#"
grid[startr - 1][startc + 1] = "2"
grid[startr][startc - 1] = "#"
grid[startr][startc]     = "#"
grid[startr][startc + 1] = "#"
grid[startr + 1][startc - 1] = "3"
grid[startr + 1][startc]     = "#"
grid[startr + 1][startc + 1] = "4"
grid = ["".join(row) for row in grid]
pos["1"] = (startr - 1, startc - 1)
pos["2"] = (startr - 1, startc + 1)
pos["3"] = (startr + 1, startc - 1)
pos["4"] = (startr + 1, startc + 1)

def isDoorOpen(n, door):
    k = ord(door) - ord("a")
    if n & (1 << k):
        return True
    else:
        return False

def openDoor(n, door):
    k = ord(door) - ord("a")
    return n | (1 << k)

@lru_cache()
def availKeys(sr, sc, doors):
    q = deque()
    ans = {}
    q.append((sr, sc))
    dp = {}
    dp[(sr, sc)] = 0

    def update(r, c, cost):
        key = (r, c)
        if (key not in dp) or dp[key] > cost:
            dp[key] = cost
            q.append(key)

    while q:
        cr, cc = q.popleft()
        cost = dp[(cr, cc)] + 1
        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            newR = cr + dr
            newC = cc + dc
            char = grid[newR][newC]

            if char == "#":
                continue
            elif char.islower():
                update(newR, newC, cost)
                if char not in ans or ans[char] > cost:
                    if not isDoorOpen(doors, char):
                        ans[char] = cost
            elif char.isupper():
                if isDoorOpen(doors, char.lower()):
                    update(newR, newC, cost)
            else:
                update(newR, newC, cost)
    return ans

q = deque()
inq = set()
dp = {}

initkey = (0, "1", "2", "3", "4")
q.append(initkey)
inq.add(initkey)
dp[initkey] = 0

def update(key, cost):
    if (key not in dp) or dp[key] > cost:
        dp[key] = cost
        if key not in inq:
            q.append(key)
            inq.add(key)

steps = 0
while q:
    steps += 1
    key = q.popleft()
    inq.remove(key)
    doors, p1, p2, p3, p4 = key
    bots = [p1, p2, p3, p4]
    cost = dp[key]

    # ans should be below prev ans
    if cost > 5000:
        continue

    # found all keys, don't keep searching
    if doors == 2 ** (len(pos) - 4) - 1:
        continue

    if steps % 10000 == 0:
        print(steps, len(q), len(dp))
        print(bin(key[0]), key[1:], cost)

    # print(bin(doors))
    for i, p in enumerate(bots):
        ppos = pos[p]
        reachable = availKeys(ppos[0], ppos[1], doors)
        # print(p, reachable)

        for k, dist in reachable.items():
            newDoors = openDoor(doors, k)
            newCost = cost + dist
            newBots = bots.copy()
            newBots[i] = k
            key = (newDoors, newBots[0], newBots[1], newBots[2], newBots[3])
            update(key, newCost)

costmin = 10 ** 8
dmax = max(map(lambda x: x[0], dp.keys()))
for (doors, _, _, _, _), v in dp.items():
    if doors == dmax:
        costmin = min(costmin, v)

print(costmin, dmax)
