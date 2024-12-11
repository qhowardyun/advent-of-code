from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

day = 5
data = get_data(day=day, year=2024)

ans = 0

rules, pages = data.split("\n\n")

prules = []

for rule in rules.splitlines():
    print(rule)

    r1, r2 = rule.split("|")
    prules.append((int(r1), int(r2)))

for line in pages.splitlines():

    nums = list(map(int, line.split(",")))

    lookup = {}

    for idx,i in enumerate(nums):
        lookup[i] = idx

    valid = True

    for r1, r2 in prules:
        if r1 not in lookup or r2 not in lookup:
            continue

        if lookup[r1] > lookup[r2]:
            valid = False
            break

    if valid:
        ans += nums[len(nums) // 2]







print(ans)
ubmit(ans, part="a", day=day, year=2024, reopen=False)
# submit(ans, part="b", day=day, year=2024, reopen=False)
