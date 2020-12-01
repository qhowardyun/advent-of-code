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

    while cpu.stdout:
        x = int(cpu.stdout.pop())
        y = int(cpu.stdout.pop())
        typ = int(cpu.stdout.pop())
        
        if x == -1 and y == 0:
            score = typ
        else:
            grid[y][x] = lookup[int(typ)]
        
        if typ == 3:
            paddlex = x
        elif typ == 4:
            ballx = x
        
        
    
    print('\n'.join([''.join([cell for cell in row]) for row in grid]))
    print("Score: ", score)
    cpu.stdin.append(int(input()))
    
    # if paddlex > ballx:
    #     cpu.stdin.append(-1)
    # elif paddlex < ballx:
    #     cpu.stdin.append(1)
    # else:
    #     cpu.stdin.append(0)
    
    # input()

print(score)