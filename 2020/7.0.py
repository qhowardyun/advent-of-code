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
for key in list(d.keys()):
    # print("d", d)
    q = set()
    ans = set()
    q.add(key)
    while q:
        print("q", q)
        cur = q.pop()
        # print(cur)
        # print(d[cur])
        for sb in d[cur]:
            q.add(sb[1])
            ans.add(sb[1])
    print(ans)
    if "shinygold" in ans:
        total += 1


print(total)

