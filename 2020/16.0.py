import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=16, year=2020)
fieldsin, mine, others = data.split("\n\n")
others = others.splitlines()[1:]

fields = {}

def inrange(num, r):
    return (r[0] <= num <= r[1]) or (r[2] <= num <= r[3])

for f in fieldsin.splitlines():
    name, data = f.split(": ")
    r1, r2 = data.split(" or ")
    r1lo, r1hi = map(int, r1.split("-"))
    r2lo, r2hi = map(int, r2.split("-"))
    fields[name] = [r1lo, r1hi, r2lo, r2hi]

print(fields)
total = 0
for other in others:
    nums = map(int, other.split(","))
    for num in nums:
        if not any(map(lambda a: inrange(num, a),fields.values())):
            total += num

print(total)


