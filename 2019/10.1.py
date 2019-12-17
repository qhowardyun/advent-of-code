from dataclasses import dataclass
from collections import defaultdict
# ax + by + c = 0

@dataclass
class Line:
    a: float
    b: float
    c: float
    
    def __hash__(self):
        return int(self.a * 1000000 + self.b * 10000 + self.c)
    
@dataclass
class Point:
    x: int
    y: int
    
def genLine(p1, p2):
    if p1.x == p2.x:
        return Line(1, 0.00000000001, -p1.x)
    
    m = (p2.y - p1.y)/(p2.x - p1.x)
    a = -m
    aa = a
    c = m*p1.x-p1.y
    
    return Line(aa, 1, c)

def lineEqual(l1, l2):
    ae = (l1.a - l2.a) <= 0.0000000000001
    ce = (l1.c - l2.c) <= 0.0000000000001

    return ae and ce and l1.b == l2.b

def dist(p1, p2):
    return (p1.x-p2.x)**2 + (p1.y-p2.y)**2

lines = open("10.in").read().strip().splitlines()
points = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            points.append(Point(x,y))

s = Point(23, 17)
# s = Point(11, 13)
points.remove(s)

lfield = defaultdict(lambda: [])
rfield = defaultdict(lambda: [])

for p in points:
    
    typ = 0
    dis = dist(s, p)
    line = genLine(p, s)
    
    if s.x == p.x:
        if s.y < p.y:
            rfield[line].append((dis, p))
        else:
            lfield[line].append((dis, p))
    elif s.x > p.x:
        rfield[line].append((dis, p))
    else:
        lfield[line].append((dis, p))
        
for key in rfield.keys():
    rfield[key].sort(key=lambda x: x[0], reverse=True)

for key in lfield.keys():
    lfield[key].sort(key=lambda x: x[0], reverse=True)
        
        
i = 1
rkeys = sorted(rfield.keys(), key=lambda x: x.a/x.b, reverse=True)
lkeys = sorted(lfield.keys(), key=lambda x: x.a/x.b, reverse=True)

grid = list(map(list, lines))
# grid[17][23] = "0"
grid[17][23] = "X"

print(len(rkeys) + len(lkeys))

# print(rkeys[0])
# print(rfield[rkeys[0]])

while True:
    
    for key in lkeys:

        if len(lfield[key]) == 0:
            lfield.pop(key)
        elif i == 201:
            print(lfield[key].pop())
            exit()
        else:
            popr = lfield[key].pop()
            point = popr[1]
            
            # print(i, point)
            grid[point.y][point.x] = str(i%9)
            # print(i, (point.y, point.x))
            # print(popr)
            # print(*("".join(line) for line in grid), sep="\n")
            # input()
            i += 1
            
    for key in rkeys:
        if len(rfield[key]) == 0:
            pass
        elif i == 201:
            print(rfield[key].pop())
            exit()
        else:
            popr = rfield[key].pop()
            point = popr[1]
            # print(i, point)
            grid[point.y][point.x] = str(i%9)
            # print(i, (point.x, point.y))
            # print(popr)
            # print(*("".join(line) for line in grid), sep="\n")
            # input()
            i += 1
        



# while i < 200:
    
    