import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=8, year=2020)
liness = data.splitlines()


def terminates(lines):
    acc = 0
    pc = 0
    visted = [False for i in range(20000)]
    while True:

        if visted[pc]:
            return False
        else:
            visted[pc] = True

        if pc >= len(lines):
            print(acc)
            return True

        line = lines[pc]
        instr, num = line.split()
        if instr == "jmp":
            pc += int(num)
        if instr == "nop":
            pc += 1
        if instr == "acc":
            pc += 1
            acc += int(num)

for i, line in enumerate(liness):
    lcopy = liness.copy()
    if "nop" in line:
        lcopy[i] = lcopy[i].replace("nop", "jmp")
    else:
        lcopy[i] = lcopy[i].replace("jmp", "nop")
    terminates(lcopy)
