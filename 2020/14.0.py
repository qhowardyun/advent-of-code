import math
import itertools
import functools
from collections import defaultdict
from aocd import get_data, submit

data = get_data(day=14, year=2020)
lines = data.splitlines()
mask = ""
mem = defaultdict(int)

for line in lines:
    # mask
    if line[1] == "a":
       mask = line.split(" = ")[1]
    else:
        addr, val = line.split(" = ")
        addr = int(addr.replace("mem[", "").replace("]", ""))
        val = format(int(val), '036b')
        newval = ""
        for v, m in zip(val, mask):
            if m == "X":
                newval += v
            else:
                newval += m
        # print(val)
        # print(mask)
        # print(newval)
        mem[addr] = int(newval, base=2)

total = 0

for k in mem.keys():
    total += mem[k]

print(total)

