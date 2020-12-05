import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=5, year=2020)
lines = data.splitlines()

def getCol(i):
    cov = "".join(i.replace("R", "1").replace("L", "0"))
    return int(cov, base = 2)

def getRow(i):
    cov = "".join(i.replace("B", "1").replace("F", "0"))
    return int(cov, base = 2)

lo = 99999
hi = 0

t = [False for i in range(1000)]

for line in lines:
    col = getCol(line[-3:])
    row = getRow(line[:-3])
    lo = min(lo, col + row * 8)
    hi = max(hi, col + row * 8)
    t[col + row* 8] = True

print("p1:", hi)

for i in range(lo, hi):
    if not t[i]:
        print("p2:", i)
        break
