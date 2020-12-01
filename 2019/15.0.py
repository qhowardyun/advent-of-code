import cpu
import copy
from collections import deque

cpu = cpu.CPU("15.in")

grid = [["?" for i in range(50)] for _ in range(46)]
dists = [[10**5 for i in range(50)] for _ in range(46)]

x = y = 23
fx = fy = None
grid[y][x] = "R"


#  1
# 3 4
#  2

q = deque([(copy.deepcopy(cpu), x, y, 0)])


def search(dir, x, y, cpu, dist):

    if dists[y][x] < dist:
        return

    
    global q
    global fx
    global fy
    
    cpu.stdin.append(dir)
    cpu.run()

    result = cpu.stdout.pop()
    
    if result == 0:
        grid[y][x] = "#"
    elif result == 1:
        grid[y][x] = "."
        q.append((copy.deepcopy(cpu), x, y, dist))
        dists[y][x] = dist
    else:
        grid[y][x] = "~"
        dists[y][x] = dist
        fx = x
        fy = y

while q:
    ccpu, x, y, dist = q.popleft()
    
    dist += 1
    
    search(1, x, y-1, copy.deepcopy(ccpu), dist)
    search(2, x, y+1, copy.deepcopy(ccpu), dist)
    search(3, x-1, y, copy.deepcopy(ccpu), dist)
    search(4, x+1, y, copy.deepcopy(ccpu), dist)
    
    # input()
    # print('\n'.join([''.join([cell for cell in row]) for row in grid]))
    
print(dists[fy][fx])