lines = open("day6.in").read().splitlines()

maxX = 498

x = [int(line.split(", ")[0]) for line in lines]
y = [int(line.split(", ")[1]) for line in lines]

grid = [[[] for _ in range(maxX)] for _ in range(maxX)]

for a, b in zip(x,y):
    for i in range(maxX):
        for j in range(maxX):
            dist = abs(a - i) + abs(b - j)
            grid[i][j].append(dist)

owners = [[-1 for _ in range(maxX)] for _ in range(maxX)]
poisoned = set()


for i in range(maxX):
    for j in range(maxX):
        least = min(grid[i][j])

        if grid[i][j].count(least) >= 2:
            owners[i][j] = 6969
        else:
            owners[i][j] = grid[i][j].index(least)

for i in range(maxX):
    poisoned.add(owners[i][0])
    poisoned.add(owners[i][maxX - 1])
    poisoned.add(owners[0][i])
    poisoned.add(owners[maxX - 1][i])

total = [0 for i in range(50)]

for i in range(maxX):
    for j in range(maxX):
        total[owners[i][j]] += 1


most = 0
print(len(total))
print(total)
total.pop()

for index, i in enumerate(total):
    if i > most and index not in poisoned:
        most = i

print(most)