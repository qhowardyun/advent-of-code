import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=9, year=2020)
lines = data.splitlines()
lines = [int(i) for i in lines]

target = 257342611

for i in range(0, len(lines)):
    for j in range(i, len(lines)):
        if sum(lines[i:j]) == target:
            a = lines[i:j]
            print(max(a) + min(a))


