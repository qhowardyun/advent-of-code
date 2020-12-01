import cpu

cpu = cpu.CPU("17.in")


cpu.run()

x = 0
y = 0

grid = []
row = ["."]

sx = sy = 0

while len(cpu.stdout) > 0:
    
    char = chr(cpu.stdout.pop())
    
    if char == "\n":
        row.append(".")
        grid.append(row)
        row = ["."]
        x = 0
        y+=1
    else:
        row.append(char)
        x+=1
        
    if char == "^":
        sx = x
        sy = y + 1
        
    # print(char, end="")

grid.insert(0, ["." for _ in range(len(grid[2]))])
grid[-1] = ["." for _ in range(len(grid[2]))]

path = []
d = 0


while True:
    
    cu = grid[sy][sx]
    
    up = grid[sy-1][sx]
    down = grid[sy+1][sx]
    left = grid[sy][sx-1]
    right = grid[sy][sx+1]
    
    if d == 0:
        if up == "#":
            path.append(1)
            sy -= 1
            
        elif left == "#":
            path.append("L")
            d -= 1
            
        elif right == "#":
            path.append("R")
            d += 1
        else:
            break
        
    elif d == 1:
        if right == "#":
            path.append(1)
            sx += 1
        elif up == "#":
            path.append("L")
            d -= 1
        elif down == "#":
            path.append("R")
            d += 1
        else:
            break
        
    elif d == 2:
        if down == "#":
            path.append(1)
            sy += 1
        elif right == "#":
            path.append("L")
            d -= 1
        elif left == "#":
            path.append("R")
            d += 1
        else:
            break
        
    elif d == 3:
        if left == "#":
            path.append(1)
            sx -= 1
        elif down== "#":
            path.append("L")
            d -= 1
        elif up == "#":
            path.append("R")
            d += 1
        else:
            break
    d %= 4


print('\n'.join([''.join([cell for cell in row]) for row in grid]))
# print(path)
# print(sx, sy)

sofar = 0

fpath = []

for p in path:
    if p == 1:
        sofar += 1
    else:
        fpath.append(sofar)
        sofar = 0
        fpath.append(p)
        
fpath.append(sofar)
        
print(*fpath, sep=",")