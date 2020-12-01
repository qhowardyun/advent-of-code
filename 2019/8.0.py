pic = open("8.in").read().strip()

w = 25
h = 6
s = w * h

ans = 0
minz = 10**9

for i in range(0, len(pic), s):
    cur = pic[i:i+s]
    
    if cur.count("0") < minz:
        minz = cur.count("0") 
        print("new min", cur.count("0"))
        ans = cur.count('1') * cur.count('2')
        
print(ans)