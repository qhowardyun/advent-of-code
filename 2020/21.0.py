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

possible = set()

for k, v in dic.items():

    ans = reduce(set.intersection, v)
    possible = possible.union(ans)
    # print(k, ans)

# print(possible)


for line in lines:
    inge, aller = line.split(" (contains ")

    inge = set(inge.split())
    aller = aller[:-1].split(", ")

    # print(inge)
    # print(aller)

    for ing in inge:
        if not ing in possible:
            total += 1
print(total)
