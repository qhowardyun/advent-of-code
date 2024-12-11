
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall

ans = 0
day = 4
data = get_data(day=day, year=2024)
lines = data.splitlines()
lines.append("." * len(lines[0]))
lines.insert(0,"." * len(lines[0]))
lines = ["." + line + "." for line in lines]

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "A":

            tr = lines[r+1][c+1]
            tl = lines[r+1][c-1]
            br = lines[r-1][c+1]
            bl = lines[r-1][c-1]

            if (tr == "M" and bl == "S") or (tr == "S" and bl == "M"):
                if (tl == "M" and br == "S") or (tl == "S" and br == "M"):
                    ans += 1



print(ans)
submit(ans, part="b", day=day, year=2024, reopen=False)
