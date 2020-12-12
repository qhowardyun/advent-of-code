import math
import itertools
import functools
from aocd import get_data, submit

data = """F10
N3
F7
R90
F11"""
data = get_data(day=12, year=2020)
lines = data.splitlines()

x = 0
y = 0
wx = 10
wy = 1
dr = 1

# 0
#3 1
# 4

for line in lines:
    print(x, y, wx, wy)
    cmd = line[0]
    amt = int(line[1:])

    if cmd == "F":
        x += wx * amt
        y += wy * amt
    elif cmd == "N":
        wy += amt
    elif cmd == "E":
        wx += amt
    elif cmd == "S":
        wy -= amt
    elif cmd == "W":
        wx -= amt
    elif cmd == "L":
        if amt == 90:
            wx, wy = -wy, wx
        elif amt == 180:
            wx, wy = -wx, -wy
        elif amt == 270:
            wx, wy = wy, -wx
    elif cmd == "R":
        if amt == 90:
            wx, wy = wy, -wx
        elif amt == 180:
            wx, wy = -wx, -wy
        elif amt == 270:
            wx, wy = -wy, wx

print(x, y, abs(x) + abs(y))
