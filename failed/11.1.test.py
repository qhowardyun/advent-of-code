grid = [[-2,-4 ,4 ,4 ,4] ,[-4 ,4 ,4 ,4 ,-5],[4 ,3 ,3 ,4 ,-4],[1 ,1 ,2 ,4 ,-3],[-1 ,0 ,2 ,-5 ,-2]]

head = []
pre = []

for row in grid:
    rowtot = 0
    for cell in row:
        print("{: d} ".format(cell), end="")
    print()