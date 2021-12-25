from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
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

    read = 6
    ans = int(ds.read(3), base=2)
    type = int(ds.read(3), base=2)

    if type == 4:
        num = ""
        last = "1"
        while last != "0":
            last = ds.read(1)
            num += ds.read(4)
            read += 5
    else:
        lti = ds.read(1)
        read += 1

        if lti == "0":
            tl = int(ds.read(15), base=2)
            read += 15
            while tl > 0:
                ver, sread = parse()
                tl -= sread
                read += sread
                ans += ver
        else:
            nsub = int(ds.read(11), base=2)
            read += 11
            for _ in range(nsub):
                ver, sread = parse()
                ans += ver
                read += sread
    return ans, read


ans, _ = parse()

submit(ans, part="a", day=day, year=2021, reopen=False)
