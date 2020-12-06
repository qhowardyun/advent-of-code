import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=6, year=2020)
lines = data.split("\n\n")

total = 0

for line in lines:
    a = set()
    line = line.replace("\n", "")
    for c in line.strip():
        a.add(c)
    print(a)
    print(len(a))
    total += len(a)
print(total)
