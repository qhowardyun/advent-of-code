from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall, finditer

day = 3
data = get_data(day=day, year=2023)

parts = {(r, c) for r, row in enumerate(data.splitlines()) for c, cell in enumerate(row) if cell not in ".1234567890"}

print(len(parts))


ans = 0
for r, line in enumerate(data.splitlines()):
    for match in finditer(r"\d+", line):

        edges = {(er, ec) for ec in range(match.start() - 1, match.end()+1) for er in (r-1, r, r+1)}

        if len(edges & parts) > 0:
            ans += int(match.group())




print(ans)
submit(ans, part="a", day=day, year=2023, reopen=False)
# submit(ans, part="b", day=day, year=2023, reopen=False)
