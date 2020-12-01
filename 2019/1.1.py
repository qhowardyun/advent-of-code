import math

lines = open("1.in").read().splitlines()

total = 0

for line in lines:

    toadd = 0
    toadd = math.floor(int(line) / 3.0) - 2
    
    while toadd > 0:
        total += toadd
        toadd = math.floor(toadd / 3.0) - 2
    
print(total)