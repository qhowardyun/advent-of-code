serialNum = 3214

grid = [[0 for _ in range(301)] for _ in range(301)]

for i in range(301):
    for j in range(301):
        rackID = i + 10
        powerLevel = rackID * j
        powerLevel += serialNum
        powerLevel *= rackID
        digits = str(powerLevel)
        grid[i][j] = int(digits[-3]) - 5

top = 0
topx, topy = 0, 0

for x in range(299):
    for y in range(299):

        total = grid[x][y]
        total += grid[x][y + 1]
        total += grid[x][y + 2]

        total += grid[x + 1][y]
        total += grid[x + 1][y + 1]
        total += grid[x + 1][y + 2]

        total += grid[x + 2][y]
        total += grid[x + 2][y + 1]
        total += grid[x + 2][y + 2]

        if total > top:
            top = total
            topx = x
            topy = y
print(topx, topy)
        
