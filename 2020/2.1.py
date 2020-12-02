import math
import itertools
import functools
from os import confstr
from aocd import get_data, submit

data = get_data(day=2, year=2020)
lines = data.splitlines()
ilines = ""

total = 0
for line in lines:
    times, letter, pas = line.split(" ")
    times = times.split("-")
    ma = int(times[0])
    mi = int(times[1])


    letter = letter[0]

    print(ma, mi)
    print(pas)
    if pas[ma - 1] == letter and pas[mi - 1] != letter:
        total += 1

    if pas[ma - 1] != letter and pas[mi - 1] == letter:
        total += 1
print(total)
submit(total)

# print(lines)
