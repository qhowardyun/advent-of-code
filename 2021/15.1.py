from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import heapq

day = 15
data = get_data(day=day, year=2021)

lines = data.splitlines()
ans = 0

q = [(0, (0, 0))]
seen = set()
best = defaultdict(lambda: 10e9)


def get_val(x, y):
    cx = x // len(lines)
    cy = y // len(lines[0])
    return (int(lines[x % len(lines)][y % len(lines[0])]) + cx + cy - 1) % 9 + 1


while q:
    cost, (x, y) = heapq.heappop(q)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(lines) * 5 and 0 <= ny < len(lines[0]) * 5:
            newcost = cost + get_val(nx, ny)
            if nx == len(lines) * 5 - 1 and ny == len(lines[0]) * 5 - 1:
                print(newcost)
                submit(newcost, part="b", day=day, year=2021, reopen=False)
                exit()
            elif best[(nx, ny)] > newcost:
                best[(nx, ny)] = newcost
                heapq.heappush(q, (newcost, (nx, ny)))
