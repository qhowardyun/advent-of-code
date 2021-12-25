from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache, reduce
import sys
import io

day = 16
data = get_data(day=day, year=2021).strip()
ans = 0

bits = ""

for h in data:
    bits += f"{int(h, base=16):04b}"

ds = io.StringIO(bits)


def parse():

    ds.read(3)
    type = int(ds.read(3), base=2)
    read = 6
    subvals = []
    val = 0

    if type == 4:
        num = ""
        last = "1"
        while last != "0":
            last = ds.read(1)
            num += ds.read(4)
            read += 5
        return int(num, base=2), read
    else:
        lti = ds.read(1)
        read += 1

        if lti == "0":
            tl = int(ds.read(15), base=2)
            read += 15
            while tl > 0:
                num, sread = parse()
                tl -= sread
                read += sread
                subvals.append(num)
        else:
            nsub = int(ds.read(11), base=2)
            read += 11
            for _ in range(nsub):
                num, sread = parse()
                read += sread
                subvals.append(num)

        if type == 0:
            val = sum(subvals)
        elif type == 1:
            val = reduce(lambda x, y: x * y, subvals)
        elif type == 2:
            val = min(subvals)
        elif type == 3:
            val = max(subvals)
        elif type == 5:
            val = 1 if subvals[0] > subvals[1] else 0
        elif type == 6:
            val = 1 if subvals[0] < subvals[1] else 0
        elif type == 7:
            val = 1 if subvals[0] == subvals[1] else 0
    return val, read


ans, _ = parse()

submit(ans, part="b", day=day, year=2021, reopen=False)
