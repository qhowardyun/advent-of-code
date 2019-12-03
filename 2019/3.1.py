from dataclasses import dataclass

in1, in2 = open("3.in").readlines()

w1 = in1.strip().split(",")
w2 = in2.strip().split(",")

min_dist = 10**7

@dataclass
class Point:
    x: int
    y: int
    steps: int
    dir: bool

# convert to pairs of nodes
def convert(wire):

    lx = 0
    ly = 0
    x = 0
    y = 0
    
    hwires = []
    vwires = []
    
    steps = 0

    for segment in wire:
        
        
        dist = int(segment[1:])
        
        horizonal = True
        dir = False
        
        if "U" in segment:
            y += dist
            horizonal = False
            dir = True
        elif "D" in segment:
            y -= dist
            horizonal = False
        elif "R" in segment:
            x += dist
            dir = True
        elif "L" in segment:
            x -= dist
        else:
            print("oops")
            
        prev = Point(lx, ly, steps, dir)
        new = Point(x, y, steps, dir)
        points = [prev, new]
        
        steps += dist
        
        if horizonal:
            points.sort(key=lambda a: a.x)
            points[1].steps += dist
            hwires.append(points)
        else:
            points.sort(key=lambda a: a.y)
            points[1].steps += dist
            vwires.append(points)
            
        lx = x
        ly = y
    
    return hwires, vwires


# test for intersections

def intersect(hwires, vwires):
    
    global min_dist
    
    for hseg in hwires:
        hp1 = hseg[0]
        hp2 = hseg[1]
        
        for vseg in vwires:
            vp1 = vseg[0]
            vp2 = vseg[1]
            
            hbound = hp1.x <= vp1.x <= hp2.x
            vbound = vp1.y <= hp1.y <= vp2.y
            
            if hbound and vbound and vp1.x is not 0 and hp2.y is not 0:
                
                poi = Point(vp1.x, hp1.y, 0, True)
                
                dx = hp1.steps 
                dy = vp1.steps
                
                # up
                if vp1.dir:
                    dy += poi.y - vp1.y
                else:
                     dy += vp2.y - poi.y
                    
                # right
                if hp1.dir:
                    dx += poi.x - hp1.x
                else:
                    dy += hp2.x - poi.x
                    
                    
                min_dist = min(dx + dy, min_dist)


w1h, w1v = convert(w1)
w2h, w2v = convert(w2)



# assume no wire on wire overlap

intersect(w1h, w2v)
intersect(w2h, w1v)

print(min_dist)