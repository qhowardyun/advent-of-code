from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
from re import search, findall
import itertools

day = 7
data = get_data(day=day, year=2024)

lines = data.splitlines()
ans = 0

times = lambda a, b: a * b
add = lambda a, b: a + b

print(len(lines))

passed = 0

for idx,line in enumerate(lines):

    target, nums = line.split(": ")
    target = int(target)

    nums = list(map(int,nums.split(" ")))

    print(idx)

    for ops in itertools.product(["*", "+"], repeat=len(nums) - 1):

        total = nums[0]
        for idx,op in enumerate(ops):
            if op == "*":
                total = total * nums[idx + 1]
            else:
                total = total + nums[idx + 1]


        if total == target:
            ans += target
            passed += 1
            break



print(ans)
assert ans != 0
input()
# submit(ans, part="b", day=day, year=2024, reopen=False)
