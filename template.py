from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 1
data = get_data(day=day, year=2021)
lines = data.splitlines()
ans = 0

print(ans)
# submit(ans, part="a", day=day, year=2021, reopen=False)
