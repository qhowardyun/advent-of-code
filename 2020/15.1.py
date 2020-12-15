import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=15, year=2020)

nums = list(map(int, data.split(",")))
# nums = [1, 3, 2]
# nums = [0, 3, 6]

lastseen = {}
lastlastseen = {}

for i, num in enumerate(nums):
    lastseen[num] = i

def addNum(num, i):
    if num in lastseen:
        lastlastseen[num] = lastseen[num]
    lastseen[num] = i
    nums.append(num)

i = len(nums) - 1
while len(nums) < 30000000:

    idx = []
    if nums[i] in lastseen:
        idx.append(lastseen[nums[i]])
    if nums[i] in lastlastseen:
        idx.append(lastlastseen[nums[i]])

    if  len(idx) != 2:
        addNum(0, i + 1)
    else:
        addNum(idx[0] - idx[1], i + 1)
    i += 1

print(nums[30000000 - 1])
