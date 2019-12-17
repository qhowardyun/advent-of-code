import cpu
import sys,tty,termios

cpu = cpu.CPU("13.in")

# hack the machine to use it for free
cpu.tape[0] = 2


grid = [["." for _ in range(40)] for _ in range(22)]
lookup = [" ", "#", "%", "W", "o"]
score = 0
paddlex = 0
ballx = 0

while not cpu.halt:
    
    cpu.run()

    while not cpu.stdout.empty():
        x = int(cpu.stdout.get())
        y = int(cpu.stdout.get())
        typ = int(cpu.stdout.get())
        
        if x == -1 and y == 0:
            score = typ
        else:
            grid[y][x] = lookup[int(typ)]
        
        if typ == 3:
            paddlex = x
        elif typ == 4:
            ballx = x
        
        
    
    # print('\n'.join([''.join([cell for cell in row]) for row in grid]))
    # print("Score: ", score)
    
    if paddlex > ballx:
        cpu.stdin.put(-1)
    elif paddlex < ballx:
        cpu.stdin.put(1)
    else:
        cpu.stdin.put(0)
    
    # input()

print(score)