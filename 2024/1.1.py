from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

ans = 0
day = 1
data = get_data(day=day, year=2024)


lines = data.splitlines()

l, r = [], []

for line in lines:
    left, right = line.split("  ")

    left = int(left)
    l.append(left)
    right = int(right)
    r.append(right)

l.sort()
r.sort()

for l, r in zip(l, r):
    ans += abs(l - r)




print(ans)
submit(ans, part="a", day=day, year=2024, reopen=False)
# submit(ans, part="b", day=day, year=2024, reopen=False)
