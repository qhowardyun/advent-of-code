import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=4, year=2020)
lines = data.splitlines()

pp = []
s = ""

for line in lines:
    if line == "":
      pp.append(s)
      s = ""
    else:
        s += " "
        s += line
total = 0

for p in pp:
    f = p.split(" ")
    fields = {}
    for d in f:
        if d == "":
            continue
        a, b = d.split(":")
        fields[a] = b
    print(fields)
    print(len(fields.keys()))
    if "byr" in fields.keys():
        if "iyr" in fields.keys():
            if "eyr" in fields.keys():
                if "hgt" in fields.keys():
                    if "hcl" in fields.keys():
                        if "ecl" in fields.keys():
                            if "pid" in fields.keys():
                                print("valid")
                                total += 1

print(total)

# print(pp)

# print(lines)

