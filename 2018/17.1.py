from collections import deque
lines = open("17.in").read().splitlines()

#0 is sand
#1 is clay
#2 is water
grid = [[0 for j in range(1846)] for i in range(800)]
maxx = 0
maxy = 0

failedlist = set()

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


def down(x, y):
    while True:
        y += 1

        #bottom of map
        if y == maxy + 1:
            return

        #hit clay
        if grid[x][y] == 1:
            y -= 1
            spreadq.add((x, y))
            return
        #keep falling
        else:
            grid[x][y] = 3

def spread(x, y):
    if(grid[x][y] == 1):
        return
    l = spreadl(x, y)
    r = spreadr(x, y)

    #both have hit walls, fill up another level
    if r == -1 and l == -1:
        grid[x][y] = 4
        spreadq.add((x, y - 1))

def spreadl(x, y):
    while grid[x + 1][y] != 1:
        x += 1
        grid[x][y] = 4
        if (x, y) in failedlist:
            failedlist.remove((x, y))
        if not grid[x][y + 1] in [1, 4]:
            downq.add((x, y))
            failedlist.add((x, y))
            return 1
    #print("spreadl -> spread", ox, y)
    return -1

def spreadr(x, y):
    while grid[x - 1][y] != 1:
        x -= 1
        grid[x][y] = 4
        if (x, y) in failedlist:
            failedlist.remove((x, y))
        if not grid[x][y + 1] in [1, 4]:
            downq.add((x, y))
            failedlist.add((x, y))
            return 1
    #print("spreadr -> spread", ox, y)
    return -1

def killr(x, y):
    while grid[x - 1][y] != 1:
        x -= 1
        grid[x][y] = 0
        if grid[x - 1][y] in [1] or (grid[x - 1][y] == 0 and grid[x - 2][y] == 0 and grid[x - 3][y] == 0):
            return
    
def killl(x, y):
    while True:
        x += 1
        grid[x][y] = 0
        if grid[x + 1][y] in [1] or (grid[x + 1][y] == 0 and grid[x + 2][y] == 0 and grid[x + 3][y] == 0):
            return


print(maxx, maxy)
sx = 500
sy = 0
grid[sx][sy] = 2
disp = [".", "█", "+", ">", "|"]

downq = set()
spreadq = set()

downq.add((sx, sy))

icount = 0

while True:
    icount += 1
    if icount % 1000 == 0:
        print(len(spreadq), len(downq))
        print(icount)
        wstr = "\n".join(["".join([disp[i] for i in row]) for row in grid])
        open("17.out", "w").write(wstr)
    if len(spreadq) > 0:
        x, y = spreadq.pop()
        spread(x, y)
    elif len(downq) > 0:
        x, y = downq.pop()
        down(x, y)
    else:
        break

for x, y in failedlist:
    killl(x, y)
    killr(x, y)

# magical stuff that makes it work
# found though inspection of output grid file
for x, row in enumerate(grid):
    for y, cell in enumerate(row):
        if cell == 4:
            if grid[x][y + 1] == 3:
                grid[x][y] = 0

wstr = "\n".join(["".join([disp[i] for i in row]) for row in grid])
open("17.out", "w").write(wstr)

for x, row in enumerate(grid):
    for y, cell in enumerate(row):
        if cell == 4:
            cx = x
            while True:
                cx += 1
                grid[cx][y] = 4
                if grid[cx + 1][y] == 1:
                    break
            cx = x
            while True:
                cx -= 1
                grid[cx][y] = 4
                if grid[cx - 1][y] == 1:
                    break

count = 0

for row in grid:
    for cell in row:
        if cell == 4:
            count += 1
wstr = "\n".join(["".join([disp[i] for i in row]) for row in grid])
open("17.out", "w").write(wstr)

#print("\n".join([" ".join([disp[i] for i in row]) for row in grid]))
#wstr = "\n".join([" ".join([disp[i] for i in row]) for row in grid])
#open("17.out", "w").write(wstr)
print(count)