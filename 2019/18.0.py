grid = list(map(list, open("18.in").read().strip().split("\n")))

from collections import deque

sx = sy = keysc = 0

for iy, row in enumerate(grid):
    for ix, cell in enumerate(row):
        if cell == '@':
            sx = ix
            sy = iy
            grid[sy][sx] = "."
        elif cell.islower():
            keysc += 1
            
print(keysc)

q = []
q.append((set(), sx ,sy, 0))

visited = [[[] for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
best = 10**9

def beat(lst, dist, keys):
    
    for l in lst:
        # print(l, dist, keys)
        if l[0] == keys and l[1] <= dist:
            return True
    
    return False

def search(keys, x, y, dist):
    
    
    tile = grid[y][x]
    if tile == "#":
        # print("wall", x, y)
        return

    # print("searching::::", keys, x, y, tile)
    
    if beat(visited[y][x], dist, keys):
        # print("failed", dist, keys)
        # print("seen", visited[y][x])
        return

    # print("visited::", "x:", x, "y:", y, keys, dist)
    visited[y][x].append((keys.copy(), dist))
    
    if tile == ".":
        q.append((keys.copy(), x, y, dist))
        
    elif tile.islower():
        
        if not tile.lower() in keys:
            
            if len(keys) + 1 == keysc:
                global best
                # print("ding ding")
                # print(dist)
                best = min(best, dist)
                return
        
            keys.add(tile)
            # print("got key", tile)
            
        q.append((keys.copy(), x, y, dist))
        
        
    elif tile.isupper():
        
        # print("need key", tile, keys)
        
        if tile.lower() in keys:
            q.append((keys, x, y, dist))
        else:
            # print("rip door", tile)
            pass
        


while q:
    
    # print("q", q)
    keys, cx, cy, dist = q.pop()
    
    if dist + 1 > best:
        continue

    dist += 1
    search(keys, cx-1, cy, dist)
    search(keys, cx+1, cy, dist)
    search(keys, cx, cy-1, dist)
    search(keys, cx, cy+1, dist)
    
print(best)