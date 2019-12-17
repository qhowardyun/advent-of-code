import math
from collections import defaultdict

raw = open("14.in").readlines()
lookup = {}
for rec in raw:
    inp, out = rec.split("=>")
    
    inpp = inp.split(",")

    amt, res = out.strip().split(" ")
    
    inlist = []
    
    for i in inpp:
        inlist.append(i.strip().split(" "))
    
    
    lookup[res] = (int(amt), inlist)


def test(aba):
    
    total = 0

    tomake = [(aba, "FUEL")]
    inv = defaultdict(int)

    while tomake:
        cur = tomake.pop()
        
        if cur[1] == "ORE":
            total += int(cur[0])
            continue
        
        needed = int(cur[0])
        item = cur[1]
        
        if item in inv:
            if inv[item] > needed:
                inv[item] -= needed
                needed = 0
            else:
                needed -= inv[item]
                inv[item] = 0
        
        reci = lookup[item]

        
        produ = int(reci[0])
        ingre = reci[1]
        
        times = -(-int(needed) // int(produ))
        
        totala = int(produ * times)
        
        # print(totala)
        inv[item] = int(inv[item] + totala - int(needed))

        for ing in ingre:
            # print(ing)
            ingcp = list(ing)
            # print(ingcp[0])
            # print(times)
            ingcp[0] = int(ingcp[0]) * int(times)
            tomake.append(ingcp)
            
    return total
            
print(test(12039407)/1000000000000)