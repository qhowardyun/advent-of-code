orbits = open("6.in").read().strip().split("\n")

pairs = []
bodies = {}

for orbit in orbits:
    a, b = orbit.split(")")
    
    pairs.append((a,b))


class Body():
    
    def __init__(self, name, count, parent):
        self.name = name
        self.parent = parent
        self.count = count
        self.children = []
            
com = Body("COM", 0, 0)
bodies["COM"] = com

while pairs:
    
    a, b = pairs.pop()
    
    if a not in bodies.keys():
        pairs.insert(0, (a, b))
        continue
    
    new_body = Body(b, bodies[a].count+1, bodies[a])
    bodies[a].children.append(new_body)
    bodies[b] = new_body
    
total = 0
target = "SAN"
cur = "YOU"

visited = set()

def search(name, i):
    
    # print(name, i)
    
    if name == "COM":
        return -696969
    
    current = bodies[name]
    
    if name in visited:
        return -10 ** 3
    
    visited.add(name)
    
    if name == target:
        print(i-2)
        exit()
    
    possible = current.children
    possible.append(current.parent)
    
    nums = []
    
    for pos in possible:
        nums.append(search(pos.name, i + 1))
    
    return max(nums)
    


search("YOU", 0)