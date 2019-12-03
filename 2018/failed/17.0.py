import queue
import sys
sys.setrecursionlimit(10000)
lines = open("17.in").read().splitlines()

#0 is sand
#1 is clay
#2 is water
grid = [[0 for j in range(1846)] for i in range(800)]
maxx = 0
maxy = 0

for line in lines:
    spl = line.split("=")
    if line[0] == "x":
        y = list(map(int, spl[2].split("..")))
        x = int(spl[1].split(",")[0])
        maxx = max(maxx, x)
        maxy = max(maxy, y[0])
        maxy = max(maxy, y[1])
        for i in range(y[0], y[1] + 1):
            grid[x][i] = 1
    else:
        x = list(map(int, spl[2].split("..")))
        y = int(spl[1].split(",")[0])
        maxy = max(maxy, y)
        maxx = max(maxx, x[0])
        maxx = max(maxx, x[1])
        for i in range(x[0], x[1] + 1):
            grid[i][y] = 1

print(maxx, maxy)
sx = 500
sy = 0

grid[sx][sy] = 2

disp = [".", "#", "+", "W", "S"]

def down(x, y):
    y += 1
    if y == maxy:
        return

    if grid[x][y] == 1:
        y -= 1
        print("down -> spread", x, y)
        spread(x, y)
    else:
        print("down -> down", x, y)
        grid[x][y] = 3
        down(x, y)

def spread(x, y):
    if(grid[x][y] in [1]):
        return
    l = spreadl(x, y)
    r = spreadr(x, y)

    if l != -1:
       #print("1")
        down(l[0], l[1])

    if r != -1:
        #print("2")
        down(r[0], r[1])
    
    if r == -1 and l == -1:
        spread(x, y - 1)

def spreadl(x, y):
    while grid[x + 1][y] != 1:
        x += 1
        if grid[x][y] == 1:
            break
        grid[x][y] = 4
        if grid[x][y + 1] == 1:
            #print("spreadl -> down", x, y)
            return x, y
    #print("spreadl -> spread", ox, y)
    return -1

def spreadr(x, y):
    while grid[x - 1][y] != 1:
        x -= 1
        if grid[x][y] == 1:
            break
        grid[x][y] = 4
        if not grid[x][y + 1] in [1, 3, 4]:
            #print("spreadr -> down", x, y)
            return x, y  
    #print("spreadr -> spread", ox, y)
    return -1


#start recursion
down(sx, sy)

count = 0

for row in grid:
    for cell in row:
        if cell == 3 or cell == 4:
            count += 1

#print("\n".join([" ".join([disp[i] for i in row]) for row in grid]))
wstr = "\n".join([" ".join([disp[i] for i in row]) for row in grid])
open("17.out", "w").write(wstr)
print(count)