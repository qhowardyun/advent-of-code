import re
from dataclasses import dataclass
import numpy
import itertools


scan = re.compile("<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>")

lines = open("12.in").readlines()

@dataclass
class vec3():
    x: int
    y: int
    z: int

pos = []

for line in lines:
    x, y, z = map(int, scan.findall(line)[0])
    pos.append(vec3(x, y, z))
    
vel = [vec3(0 ,0, 0) for _ in range(len(pos))]

xinit = [p.x for p in pos]
yinit = [p.y for p in pos]
zinit = [p.z for p in pos]

xlcm = 0
ylcm = 0
zlcm = 0

i = 1

xdone = ydone = zdone = False

while not (xdone and ydone and zdone):

    for at, bt in itertools.combinations(zip(pos, vel), 2):
        
        a, va = at
        b, vb = bt
        
        if a.x > b.x:
            va.x -= 1
            vb.x += 1
        elif b.x > a.x:
            va.x += 1
            vb.x -= 1
            
        if a.y > b.y:
            va.y -= 1
            vb.y += 1
        elif b.y > a.y:
            va.y += 1
            vb.y -= 1
            
        if a.z > b.z:
            va.z -= 1
            vb.z += 1
        elif b.z > a.z:
            va.z += 1
            vb.z -= 1
            
            
    for posi, veli in zip(pos, vel):
        
        posi.x += veli.x
        posi.y += veli.y
        posi.z += veli.z

    # print(*pos, sep="\n")
    # print("vel:")
    # print(*vel, sep="\n")
    # input()

    xl = []
    yl = []
    zl = []
    
    for p in pos:
        xl.append(p.x)
        yl.append(p.y)
        zl.append(p.z)
        
    if not xdone and xl == xinit:
        xlcm = i + 1
        xdone = True
    if not ydone and yl == yinit:
        ylcm = i + 1
        ydone = True
    if not zdone and zl == zinit:
        zlcm = i + 1
        zdone = True
        
    i += 1
        
total = 0

print(xlcm, ylcm, zlcm)
print(numpy.lcm(zlcm, numpy.lcm(ylcm, xlcm)))