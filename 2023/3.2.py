from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall, finditer

day = 3
data = get_data(day=day, year=2023)
data = data.splitlines()

parts = {(r, c): [] for r, row in enumerate(data) for c, cell in enumerate(row) if cell not in ".1234567890"}


ans = 0
for r, line in enumerate(data):
    for match in finditer(r"\d+", line):

        edges = {(er, ec) for ec in range(match.start() - 1, match.end()+1) for er in (r-1, r, r+1)}

        for k in edges & parts.keys():
            parts[k].append(int(match.group()))

for (r, c), v in parts.items():
    if data[r][c] == "*" and len(v) == 2:
        prod = 1
        for x in v:
            prod *= x

        ans += prod

print(ans)
# submit(ans, part="a", day=day, year=2023, reopen=False)
submit(ans, part="b", day=day, year=2023, reopen=False)
