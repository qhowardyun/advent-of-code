
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

day = 5
data = get_data(day=day, year=2024)

ans = 0

rules, pages = data.split("\n\n")

prules = []
drules = defaultdict(int)

wrong = []

for rule in rules.splitlines():
    print(rule)

    r1, r2 = rule.split("|")
    r1, r2 = int(r1), int(r2)
    prules.append((int(r1), int(r2)))

    drules[(r1, r2)] = -1
    drules[(r2, r1)] = 1

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
            wrong.append(nums)
            break

from functools import cmp_to_key


print(wrong)

def compare(x1, x2):
    return drules[(x1, x2)]

for line in wrong:
    s = sorted(line, key=cmp_to_key(compare))
    ans += s[len(s)//2]








print(ans)
submit(ans, part="b", day=day, year=2024, reopen=False)
