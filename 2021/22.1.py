from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import re

day = 22
data = get_data(day=day, year=2021)
lines = data.splitlines()

X = set()
Y = set()
Z = set()

cmds = []
for line in lines:
    x1, x2, y1, y2, z1, z2 = list(map(int, re.findall(r"-?\d+", line)))
    X.add(x1)
    X.add(x2 + 1)
    Y.add(y1)
    Y.add(y2 + 1)
    Z.add(z1)
    Z.add(z2 + 1)
    cmds.append((x1, x2, y1, y2, z1, z2, line.startswith("on")))


def transform(x):
    cords = sorted(list(x))
    m = {}
    for i, v in enumerate(cords):
        m[v] = i

    diff = [b - a for a, b in zip(cords, cords[1:])]
    return m, diff


X, DX = transform(X)
Y, DY = transform(Y)
Z, DZ = transform(Z)


cubes = set()
cmd_len = len(cmds)
for i, (x1, x2, y1, y2, z1, z2, turn_on) in enumerate(cmds):
    print(len(cubes), i / cmd_len)
    for x in range(X[x1], X[x2 + 1]):
        for y in range(Y[y1], Y[y2 + 1]):
            for z in range(Z[z1], Z[z2 + 1]):
                point = (x, y, z)
                if turn_on:
                    cubes.add(point)
                else:
                    cubes.discard(point)


ans = 0

print(len(X))
print(len(DX))
print(len(Z))
print(len(DZ))

for x, y, z in cubes:
    lx = DX[x]
    ly = DY[y]
    lz = DZ[z]
    ans += lx * ly * lz


print(ans)
