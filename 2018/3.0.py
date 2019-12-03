lines = open("day3.in").read().splitlines()
x = []
y = []
w = []
h = []
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    _, _, coord, size = line.split()


    xin, yin = coord[:-1].split(",")
    win, hin = size.split("x")

    x.append(int(xin))
    y.append(int(yin))
    w.append(int(win))
    h.append(int(hin))


for x, y, w, h in zip(x,y,w,h):
    for i in range(x, x + w):
        for j in range(y, y + h):
            grid[i][j] += 1

#print('\n'.join(' '.join([str(cell) for cell in row]) for row in grid))

overlap = 0

for row in grid:
    for cell in row:
        if cell > 1:
            overlap += 1

print(overlap)