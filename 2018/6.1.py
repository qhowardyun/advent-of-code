lines = open("day6.in").read().splitlines()

maxX = 497

x = [int(line.split(", ")[0]) for line in lines]
y = [int(line.split(", ")[1]) for line in lines]

#grid = [[[] for _ in range(maxX)] for _ in range(maxX)]

plane = 0

for i in range(maxX):
    for j in range(maxX):

        dist = 0
        for a, b in zip(x,y):
            dist += (abs(a - i) + abs(b - j))
        if dist < 10000:
            plane += 1

print(plane)
