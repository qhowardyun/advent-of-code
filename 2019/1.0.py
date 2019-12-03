import math

lines = open("1.in").read().splitlines()

total = 0

for line in lines:
    total += math.floor(int(line) / 3.0) - 2
    
print(total)

