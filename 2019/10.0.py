from dataclasses import dataclass

# ax + by + c = 0

@dataclass
class Line:
    a: float
    b: float
    c: float
    
    def __hash__(self):
        return int(self.a * 10000 + self.b * 100 + self.c)
    
@dataclass
class Point:
    x: int
    y: int
    
def genLine(p1, p2):
    if p1.x == p2.x:
        return Line(1, 0, -p1.x)
    
    m = (p2.y - p1.y)/(p2.x - p1.x)
    a = -m
    c = m*p1.x-p1.y
    
    return Line(a, 1, c)

def lineEqual(l1, l2):
    ae = (l1.a - l2.a) <= 0.000000001
    ce = (l1.c - l2.c) <= 0.000000001

    return ae and ce and l1.b == l2.b

lines = open("10.in").read().strip().splitlines()
points = []

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == "#":
            points.append(Point(x,y))

maxsf = 0
point = 0

for o in points:
    vison = set()
    
    pcopy = points.copy()
    pcopy.remove(o)
    for a in pcopy:
        
        typ = ""
        if o.x == a.x:
            typ = "a" if o.y > a.y else "b"
        else:
            typ = "l" if o.x < a.x else "r"
            
        vison.add((typ,genLine(o, a)))
    
    if len(vison) >= maxsf:
        point = o
    
    maxsf = max(maxsf, len(vison))

print(maxsf)
print(point)