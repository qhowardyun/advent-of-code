import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=6, year=2020)
lines = data.split("\n\n")

total = 0

for line in lines:
    ans = []
    for res in line.strip().split("\n"):
        a = set()
        for c in res:
            a.add(c)
        ans.append(a)
    ta = functools.reduce(lambda a, b: a.intersection(b), ans)
    total += len(ta)
print(total)
