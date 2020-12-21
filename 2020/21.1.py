import math
from functools import reduce
from typing import DefaultDict
from aocd import get_data, submit

data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
data = get_data(day=21, year=2020)
lines = data.splitlines()

dic = DefaultDict(list)

total = 0

for line in lines:
    inge, aller = line.split(" (contains ")

    inge = set(inge.split())
    aller = aller[:-1].split(", ")

    # print(inge)
    # print(aller)

    for al in aller:
        dic[al].append(inge)

possible = {}

for k, v in dic.items():

    ans = reduce(set.intersection, v)
    possible[k] = ans
    # print(k, ans)

# print(possible)

# print("____________")

danger = {}

while True:
    if len(possible) == 0:
        break

    for k, v in list(possible.items()):
        if len(v) == 1:
            found = v.pop()
            # print("found", found)
            danger[k] = found
            possible.pop(k)

            for ki, vi in possible.items():
                if found in vi:
                    vi.remove(found)
            break
# print(danger)

print(",".join([danger[k] for k in sorted(danger.keys())]))
