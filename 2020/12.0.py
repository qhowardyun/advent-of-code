import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=12, year=2020)
data = """F10
N3
F7
R90
F11"""
lines = data.splitlines()

x = 0
y = 0
dr = 1

# 0
#3 1
# 4

for line in lines:
    print(x, y)
    cmd = line[0]
    amt = int(line[1:])

    if cmd == "F":
        if dr == 0:
            cmd = "N"
        if dr == 1:
            cmd = "E"
        if dr == 2:
            cmd = "S"
        if dr == 3:
            cmd = "W"

    if cmd == "N":
        y += amt
    elif cmd == "E":
        x += amt
    elif cmd == "S":
        y -= amt
    elif cmd == "W":
        x -= amt
    elif cmd == "L":
        dr -= amt / 90
    elif cmd == "R":
        dr += amt / 90
    dr %= 4

print(x, y, abs(x) + abs(y))
