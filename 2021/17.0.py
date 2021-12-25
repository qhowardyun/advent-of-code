from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import re

day = 17
data = get_data(day=day, year=2021)

x1, x2, y1, y2 = list(map(int, re.findall(r"-?\d+", data)))


def check(vx, vy):
    x, y = 0, 0
    my = 0
    while True:
        x += vx
        y += vy
        my = max(my, y)

        if x1 <= x <= x2 and y1 <= y <= y2:
            return True, my

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if (vx > 0 and x > x2) or (vx < 0 and x < x1) or (vy < 0 and y < y2):
            return False, None


maxmaxy = 0

for dx in range(x2):
    for dy in range(4 * x2):
        valid, maxy = check(dx, dy)
        if valid:
            maxmaxy = max(maxmaxy, maxy)

submit(maxmaxy, part="a", day=day, year=2021, reopen=False)
