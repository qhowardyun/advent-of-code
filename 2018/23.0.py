import math
import itertools
import functools
from z3 import *
import re
from aocd import get_data, submit

data = get_data(day=23, year=2018)
lines = data.splitlines()
# pattern = re.compile(r'pos=<([0-9]+),([0-9]+),(\d+)>, r=(\d+)/')
pattern = re.compile(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")

bots = []
maxR = 0
maxRI = 0
i = 0

for line in lines:
    x, y, z, r = map(int, pattern.match(line).groups())

    if r > maxR:
        maxR = r
        maxRI = i
    i += 1
    bots.append((x, y, z, r))

mbx, mby, mbz, mbr = bots[maxRI]
total = 0
for bot in bots:
    x, y, z, _ = bot
    if abs(mbx - x) + abs(mby - y) + abs(mbz - z) <= mbr:
        total += 1
print("p1: ", total)


def zabs(x):
    return If(x >= 0, x, -x)


x = Int("x")
y = Int("y")
z = Int("z")

# magic Z3 solver box
isInRanges = [Int(str(i) + " isInRange") for i in range(len(bots))]
count = Int("sum")
s = Optimize()

for i, (bx, by, bz, br) in enumerate(bots):
    rangeIf = If(zabs(x - bx) + zabs(y - by) + zabs(z - bz) <= br, 1, 0)
    s.add(isInRanges[i] == rangeIf)
s.add(count == sum(isInRanges))

originDist = Int("dist")
s.add(originDist == zabs(x) + zabs(y) + zabs(z))

s.maximize(count)
ans = s.minimize(originDist)

s.check()

print(s.lower(ans))
print(s.sexpr())
