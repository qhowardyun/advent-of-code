import math
import itertools
import functools
import re
from collections import defaultdict
from aocd import get_data, submit

data = get_data(day=7, year=2020)
lines = data.splitlines()

d = defaultdict(list)

for line in lines:
    if "no other bags" in line:
        continue
    line = line.replace(".", "")
    line = line.replace(" bags", "")
    line = line.replace(" bag", "")
    a, b = line.split("contain")
    a = "".join(a.split(" "))
    b = b.split(",")
    for r in b:
        # print(r)
        c, b1, b2 = r.split()
        d[a].append((int(c), b1+b2))

total = 0
q = []
q.append("shinygold")
while q:
    print(q)
    cur = q.pop()
    for sb in d[cur]:
        for i in range(sb[0]):
            q.append(sb[1])
        total += sb[0]

print(total)

