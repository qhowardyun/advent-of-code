lines = open("day3.in").read().splitlines()

x = []
y = []
w = []
h = []
ID = []
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:

    IDin, _, coord, size = line.split()
    xin, yin = coord[:-1].split(",")
    win, hin = size.split("x")

    x.append(int(xin))
    y.append(int(yin))
    w.append(int(win))
    h.append(int(hin))
    ID.append(int(IDin[1:]))

for xi, yi, wi, hi in zip(x,y,w,h):
    for i in range(xi, xi + wi):
        for j in range(yi, yi + hi):
            grid[i][j] += 1

#print('\n'.join(' '.join([str(cell) for cell in row]) for row in grid))

for IDi, xi, yi, wi, hi in zip(ID, x,y,w,h):
    valid = True
    for i in range(xi, xi + wi):
        for j in range(yi, yi + hi):
            if grid[i][j] != 1:
                valid = False
                break
    if valid:
        print(IDi)