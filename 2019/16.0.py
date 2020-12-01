l = list(map(int, list(open("16.in").read())))
new_l = []

pattern = [0, 1, 0, -1]

for _ in range(3):
    for i in range(1, len(l)+1):
    
        cur_pattern = [0]*i + [1]*i + [0]*i + [-1]*i
        plen = len(cur_pattern)
        
        d = 0
        
        for i, num in enumerate(l):
            # print(num, "*", cur_pattern[(i+1)%plen])
            d += num * cur_pattern[(i+1)%plen]
            
        d = abs(d) % 10
        
        new_l.append(d)
    
    l = new_l
    new_l = []
    
    # print('done')
    print(*l, sep="")