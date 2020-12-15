import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=15, year=2020)

nums = list(map(int, data.split(",")))
# nums = [1, 3, 2]
# nums = [0, 3, 6]

i = len(nums) - 1
while len(nums) < 2022:
    idx = [j for j in range(len(nums)) if nums[j] == nums[i]]
    if  len(idx) < 2:
        nums.append(0)
    else:
        nums.append(idx[-1] - idx[-2])
    i += 1

print(nums[2019])
