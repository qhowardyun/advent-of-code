import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=9, year=2020)
lines = data.splitlines()
lines = [int(i) for i in lines]

for i in range(25, len(lines)):

    valid = False
    for  j in range(i - 25, i):
        for  k in range(j, i):
            if lines[j] + lines[k] == lines[i]:
                # print(i, j, k)
                valid = True
    if not valid:
        print(lines[i])
