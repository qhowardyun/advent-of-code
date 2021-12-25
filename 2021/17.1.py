from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import re

day = 17
data = get_data(day=day, year=2021)
# data = "target area: x=20..30, y=-10..-5"
ans = 0

x1, x2, y1, y2 = list(map(int, re.findall(r"-?\d+", data)))


def check(vx, vy):
    x, y = 0, 0
    while True:
        x += vx
        y += vy

        if x1 <= x <= x2 and y1 <= y <= y2:
            return True

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if x > x2 or (vy < 0 and y < y1):
            return False


for dx in range(2 * x2):
    for dy in range(y2 * 2, -y2 * 2):
        valid = check(dx, dy)
        if valid:
            ans += 1
print(ans)
submit(ans, part="b", day=day, year=2021, reopen=False)
