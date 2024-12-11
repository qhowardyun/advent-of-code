from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

day = 2
data = get_data(day=day, year=2024)

lines = data.splitlines()

ans = 0

for line in lines:
    levels = list(map(int, line.split(" ")))

    safe = True
    diffs = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

    positive = [x for x in diffs if x > 0]
    negative = [x for x in diffs if x < 0]

    bad = [x for x in diffs if abs(x) < 1 or abs(x) > 3]

    print(line)
    print(diffs)
    print(positive, negative, bad)

    if len(positive) != len(diffs) and len(negative) != len(diffs):
        safe = False

    if len(bad) > 0:
        safe = False

    if safe:
        ans += 1



# print(lines)




print(ans)
submit(ans, part="a", day=day, year=2024, reopen=False)
# submit(ans, part="b", day=day, year=2024, reopen=False)
