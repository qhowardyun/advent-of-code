import sys

lines = open("day1.in").read().splitlines()
current = 0
used = set()
nums = []

for line in lines:
    nums.append(int(line.replace("+", "")))

while True:
    for num in nums:
        current += num
        if current in used:
            print(current)
            sys.exit()
        used.add(current)

print(used)