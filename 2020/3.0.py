import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=3, year=2020)
lines = data.splitlines()
ilines = ""

r = 0
c = 0
total = 0
mod = len(lines[0])

while True:
    print(r, c)
    if lines[r][c % mod] == "#":
        total += 1
    c += 3
    r += 1
    print(total)
    if r > len(lines):
        break
print(total)

print(lines)

