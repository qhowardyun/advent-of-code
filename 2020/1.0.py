import math
import itertools
import functools
from os import confstr
from aocd import get_data, submit

data = get_data(day=1, year=2020)
lines = data.splitlines()

ilines = [int(i) for i in lines]

for a in ilines:
    for b in ilines:
            if a + b == 2020:
                print(a, b)
                submit(a * b, part="a", day=1, year=2020)
