import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=10, year=2020)
lines = data.splitlines()
lines = [int(x) for x in lines]

lines = sorted(lines)
target = max(lines)

dp = [0 for _ in range(target + 1)]
dp[0] = 1
for i in lines:
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

print(dp[target])

