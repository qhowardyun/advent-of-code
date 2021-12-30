from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import re

day = 22
data = get_data(day=day, year=2021)
lines = data.splitlines()
ans = 0

print(ans)
# submit(ans, part="a", day=day, year=2021, reopen=False)

cubes = set()

for line in lines:
    x1, x2, y1, y2, z1, z2 = list(map(int, re.findall(r"-?\d+", line)))

    if abs(x1) > 50:
        continue

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                point = (x, y, z)
                if line.startswith("on"):
                    cubes.add(point)
                else:
                    if point in cubes:
                        cubes.remove(point)


print(len(cubes))
