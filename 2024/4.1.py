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

for dr in [1, 0 , -1]:
    for dc in [1, 0, -1]:
        if dr == 0 and dc == 0:
            continue

        x = set()
        m = set()
        a = set()
        s = set()
        tests = [(x, "M", m), (m, "A", a), (a, "S", s)]

        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "X":
                    x.add((r, c))

        for x, char, y in tests:
            for r, c in x:
                nr, nc = r + dr, c + dc
                if lines[nr][nc] == char:
                    y.add((nr, nc))

        ans += len(s)


submit(ans, part="a", day=day, year=2024, reopen=False)
# submit(ans, part="b", day=day, year=2024, reopen=False)
