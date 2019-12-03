class Vect:

    x = 0
    y = 0

    xvel = 0
    yvel = 0

    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
    
    def update(self):
        self.x += self.xvel
        self.y += self.yvel

lines = open("10.in").read().splitlines()

points = []

for i in lines:
    parts = i[10:].split(",")
    bits = parts[1].split("=")

    x = int(parts[0])
    y = int(bits[0][:-10])

    velx = int(bits[1][1:])
    vely = int(parts[2][:-1])

    #print(x, y, velx, vely)

    points.append(Vect(x, y, velx, vely))

count = 0

for i in range(10820):
    for point in points:
        point.update()

for i in range(10000):
    for point in points:
        point.update()

    grid = [[" " for _ in range(300)] for _ in range(300)]

    maxx = 0
    maxy = 0
    minx = 1000000
    miny = 1000000

    for point in points:
        maxx = max(maxx, point.x)
        maxy = max(maxy, point.y)
        minx = min(minx, point.x)
        miny = min(miny, point.y)

        x = int((point.x) + 20)
        y = int((point.y) + 20)
        
        #print(x,y)
        grid[y][x] = "#"

    open("out.txt", "w").write('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
    #print(maxx, maxy, minx, miny)
    count += 1
    #print(count)
    input()


    

