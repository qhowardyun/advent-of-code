import math
import itertools
import functools
from collections import deque
from aocd import get_data, submit

data = get_data(day=23, year=2020)
cups = deque()

for c in data:
    cups.append(int(c))

SIZE = len(cups)

for _ in range(100):
    selected = cups.popleft()
    c1, c2, c3 = cups.popleft(), cups.popleft(), cups.popleft()
    dest = selected - 1
    if dest == 0:
        dest = SIZE
    while dest in [c1, c2, c3]:
        dest -= 1
        if dest == 0:
            dest = SIZE
    insidx = cups.index(dest) + 1
    cups.insert(insidx, c3)
    cups.insert(insidx, c2)
    cups.insert(insidx, c1)
    cups.append(selected)

while cups[0] != 1:
    cups.rotate(1)

print("".join([str(x) for x in list(cups)[1:]]))
