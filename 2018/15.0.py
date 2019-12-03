lines = open("day15.in").read().splitlines()

grid = []
g = []
e = []

for line in lines:
    grid.append([i for i in line])

#grid[y][x]


for row in grid:
    for i in row:
        print(i)
rounds = 0

while True:

    



    rounds += 1

if len(g) == 0:
    print(sum(e))
    print(rounds * sum(e))
else:
    print(sum(g))
    print(rounds * sum(g))