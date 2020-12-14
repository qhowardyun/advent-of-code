import math
import itertools
import functools
from collections import defaultdict
from aocd import get_data, submit

data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
data = get_data(day=14, year=2020)
lines = data.splitlines()
mask = ""
mem = defaultdict(int)

def assign(addr, val):
    if addr.count("X") == 0:
        # print(addr, val)
        mem[int(addr)] = val
    else:
        xi = addr.find("X")
        c1 = list(addr)
        c1[xi] = "1"
        c2 = list(addr)
        c2[xi] = "0"
        assign("".join(c1), val)
        assign("".join(c2), val)


for line in lines:
    # mask
    if line[1] == "a":
       mask = line.split(" = ")[1]
    else:
        addr, val = line.split(" = ")
        addr = int(addr.replace("mem[", "").replace("]", ""))
        addr = format(int(addr), '036b')
        val = int(val)
        newaddr = ""
        for v, m in zip(addr, mask):
            if m == "X":
                newaddr += "X"
            elif m == "0":
                newaddr += v
            else:
                newaddr += "1"
        assign(newaddr, val)

total = 0

for k in mem.keys():
    total += mem[k]

print(total)

