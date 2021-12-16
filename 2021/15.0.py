from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import heapq

day = 15
data = get_data(day=day, year=2021)
grid = data.splitlines()
ans = 0

q = [(0, (0, 0))]
seen = set()
best = defaultdict(lambda: 10e9)

while q:
    cost, (x, y) = heapq.heappop(q)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            newcost = cost + int(grid[nx][ny])
            if nx == len(grid) - 1 and ny == len(grid[0]) - 1:
                print(newcost)
                submit(newcost, part="a", day=day, year=2021, reopen=False)
                exit()
            elif best[(nx, ny)] > newcost:
                best[(nx, ny)] = newcost
                heapq.heappush(q, (cost + int(grid[nx][ny]), (nx, ny)))
