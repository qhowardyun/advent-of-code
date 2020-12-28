from aocd import get_data
import cpu

sx, sy = 5, 4
SIZE = 100

def inBeam(x, y):
    program = cpu.CPU("19.in")
    program.stdin.append(x)
    program.stdin.append(y)
    program.run()
    return program.stdout.pop() == 1

def goNext():
    global sx, sy
    sx += 1
    sy += 2
    while not inBeam(sx, sy):
        sy -= 1

while True:
    goNext()
    cx = sx + (SIZE - 1)
    cy = sy - (SIZE - 1)
    if cy >= 0 and inBeam(cx, cy):
        break
print(10000 * sx + cy)

