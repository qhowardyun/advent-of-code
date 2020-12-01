orbits = open("6.in").read().strip().split("\n")

pairs = []
bodies = {}

for orbit in orbits:
    a, b = orbit.split(")")
    
    pairs.append((a,b))


class Body():
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.children = []
            
com = Body("COM", 0)
bodies["COM"] = com

while pairs:
    
    a, b = pairs.pop()
    
    if a not in bodies.keys():
        pairs.insert(0, (a, b))
        continue
    
    new_body = Body(b, bodies[a].count+1)
    bodies[a].children.append(new_body)
    bodies[b] = new_body
    
total = 0

for body in bodies.values():
    total += body.count
    
print(total)
            
    