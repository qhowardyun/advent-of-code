import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=2, year=2020)
lines = data.splitlines()
ilines = ""

try:
    ilines = [int(x) for x in lines]
except:
    pass

print(lines)

