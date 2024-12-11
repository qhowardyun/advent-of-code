from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

day = 2
data = get_data(day=day, year=2024)

# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

lines = data.splitlines()

ans = 0

for line in lines:
    levels = list(map(int, line.split(" ")))

    safe = False

    for i in range(len(levels)):
        if safe:
            continue
        il = levels.copy()
        il.pop(i)
        diffs = [il[j] - il[j - 1] for j in range(1, len(il))]

        positive = [x for x in diffs if x > 0]
        negative = [x for x in diffs if x < 0]

        good = [x for x in diffs if abs(x) >= 1 and abs(x) <= 3]

        print(il)
        print(diffs)
        print(positive, negative, good)

        if len(positive) == len(diffs) or len(negative) == len(diffs):
            if len(good) == len(diffs):
                safe = True

    il = levels.copy()
    diffs = [il[j] - il[j - 1] for j in range(1, len(il))]

    positive = [x for x in diffs if x > 0]
    negative = [x for x in diffs if x < 0]

    good = [x for x in diffs if abs(x) >= 1 and abs(x) <= 3]

    print(il)
    print(diffs)
    print(positive, negative, good)

    if len(positive) == len(diffs) or len(negative) == len(diffs):
        if len(good) == len(diffs):
            safe = True

    if safe:
        ans += 1



# print(lines)




print(ans)
# submit(ans, part="a", day=day, year=2024, reopen=False)
submit(ans, part="b", day=day, year=2024, reopen=False)
