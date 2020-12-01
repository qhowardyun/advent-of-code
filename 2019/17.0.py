import cpu

cpu = cpu.CPU("17.in")


cpu.run()

x = 0
y = 0

grid = []
row = ["."]

while len(cpu.stdout) > 0:
    
    char = chr(cpu.stdout.pop())
    
    if char == "\n":
        row.append(".")
        grid.append(row)
        row = ["."]
    else:
        row.append(char)
        
    # print(char, end="")

grid.insert(0, ["." for _ in range(len(grid[2]))])
grid[-1] = ["." for _ in range(len(grid[2]))]

total = 0  

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "#":
            right = grid[y][x+1] == "#"
            left = grid[y][x-1] == "#"
            up = grid[y+1][x] == "#"
            down = grid[y-1][x] == "#"
            if right and left and up and down:
                total += (x-1)*(y-1)

print(total)
# print('\n'.join([''.join([cell for cell in row]) for row in grid]))