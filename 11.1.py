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
topx, topy, tops = 0, 0, 0

for s in range(15):
    print(s)
    for x in range(300 - s):
        for y in range(300 - s):
            
            total = 0
            #sum
            for i in range(x, x + s):
                for j in range(y, y + s):
                    total += grid[i][j]

            if total > top:
                top = total
                topx = x
                topy = y
                tops = s
        

print(topx, topy, tops)
        
