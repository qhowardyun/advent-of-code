from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

day = 1
data = get_data(day=day, year=2024)

lines = data.splitlines()
lines = [int(x) for x in lines]
ans = 0

for line in lines:
    pass



print(ans)
assert ans != 0
input()
submit(ans, part="a", day=day, year=2024, reopen=False)
# submit(ans, part="b", day=day, year=2024, reopen=False)
