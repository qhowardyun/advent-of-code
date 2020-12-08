import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=8, year=2020)
lines = data.splitlines()

acc = 0
pc = 0
visted = [False for i in range(20000)]

while True:

    if visted[pc]:
        break
    else:
        visted[pc] = True


    instr, num = lines[pc].split()
    if instr == "jmp":
        pc += int(num)
    if instr == "nop":
        pc += 1
    if instr == "acc":
        pc += 1
        acc += int(num)

print(acc)
