import re
from dataclasses import dataclass
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

for i in range(1000):

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


total = 0

for p, v in zip(pos, vel):
    total += (abs(v.y) + abs(v.x) + abs(v.z)) * (abs(p.x) + abs(p.y) + abs(p.z))
    
print(total)