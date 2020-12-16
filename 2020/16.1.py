from collections import defaultdict
import math
import itertools
import functools
from typing import DefaultDict
from aocd import get_data, submit

data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
data = get_data(day=16, year=2020)
fieldsin, mine, others = data.split("\n\n")
others = others.splitlines()[1:]

fields = {}

def inrange(num, r):
    return (r[0] <= num <= r[1]) or (r[2] <= num <= r[3])

def isvalid(nums, r):
    return all([inrange(num, r) for num in nums])

for f in fieldsin.splitlines():
    name, data = f.split(": ")
    r1, r2 = data.split(" or ")
    r1lo, r1hi = map(int, r1.split("-"))
    r2lo, r2hi = map(int, r2.split("-"))
    fields[name] = [r1lo, r1hi, r2lo, r2hi]

total = 0
good = []
for other in others:
    nums = list(map(int, other.split(",")))
    goodg = True
    for num in nums:
        if not any(map(lambda a: inrange(num, a), fields.values())):
            goodg = False
            break
    if goodg:
        good.append(nums)

field = 0

valididx = defaultdict(list)


for k, v in fields.items():
    for i in range(len(good[0])):
        values = []

        # print("testing", k, " on row", i)
        for j in range(len(good)):
            values.append(good[j][i])
        if isvalid(values, v):
            valididx[k].append(i)

taken = set()
f_to_idx = {}

while True:
    if len(valididx) == 0:
        break

    key = min(valididx.items(), key=lambda x: len(x[1]))[0]
    location = valididx[key].pop()
    while location in taken:
        location = valididx[key].pop()

    taken.add(location)
    f_to_idx[key] = location
    valididx.pop(key)

mine = mine.splitlines()[1]
mine = list(map(int, mine.split(",")))

total = 1

for k, v in fields.items():
    if "departure" in k:
        total *= mine[f_to_idx[k]]

print(total)
