pic = open("8.in").read().strip()

w = 25
h = 6
s = w * h

ans = 0
minz = 10**9


images = []
tex = [".", "#"]

for i in range(0, len(pic), s):
    cur = pic[i:i+s]
    images.append(cur)
    
print(len(images[54]))

images.reverse()

for j in range(6):
    for i in range(25):
        cur = 1
        for img in images:
            if img[i+j*25] == "1":
                cur = 1
            elif img[i+j*25] == "0":
                cur = 0
        print(tex[cur], end="")
    print()