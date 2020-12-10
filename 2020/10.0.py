import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=10, year=2020)
lines = data.splitlines()
lines = [int(x) for x in lines]

lines = sorted(lines)

lines.insert(0, 0)
lines.append(max(lines) + 3)

s = 0
t = 0

for i in range(1, len(lines)):
    diff = lines[i] - lines[i-1]
    if diff == 3:
        t += 1
    if diff == 1:
        s += 1
print(s * t)


