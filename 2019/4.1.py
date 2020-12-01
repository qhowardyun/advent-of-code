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
    
    dd1 = d1 == d2 and not d2 == d3
    dd2 = (not d1 == d2) and d2 == d3 and not d3 == d4
    dd3 = (not d2 == d3) and d3 == d4 and not d4 == d5
    dd4 = (not d3 == d4) and d4 == d5 and not d5 == d6
    dd5 = (not d4 == d5) and d5 == d6
    
    increase = (d1 <= d2 and d2 <= d3 and d3 <= d4 and d4 <= d5 and d5 <= d6)
    
    if (dd1 or dd2 or dd3 or dd4 or dd5) and increase:
            # print(i)
            count += 1
        
print(count)