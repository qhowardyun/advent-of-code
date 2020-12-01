import cpu

cpu = cpu.CPU("13.in")

cpu.run()

grid = [["." for _ in range(50)] for _ in range(24)]
lookup = [" ", "#", "%", "_", "o"]


while not cpu.stdout.empty():
    
    x = cpu.stdout.get()
    y = cpu.stdout.get()
    typ = cpu.stdout.get()
    grid[int(y)][int(x)] = lookup[int(typ)]
    print('\n'.join([''.join([cell for cell in row]) for row in grid]))
    input()


count = 0    

for line in grid:
    for cell in line:
        if cell == "%":
            count += 1
            
print(count)