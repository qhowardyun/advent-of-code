minr = 134564
maxr = 585159

count = 0

for i in range(minr, maxr):

    snum = str(i)
    d1 = int(snum[0])
    d2 = int(snum[1])
    d3 = int(snum[2])
    d4 = int(snum[3])
    d5 = int(snum[4])
    d6 = int(snum[5])
    
    double = d1 == d2 or d2 == d3 or d3 == d4 or d4 == d5 or d5 == d6
    increase = (d1 <= d2 and d2 <= d3 and d3 <= d4 and d4 <= d5 and d5 <= d6)

    if double and increase:
        count += 1
        
print(count) 