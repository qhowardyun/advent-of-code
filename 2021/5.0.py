from aocd import get_data, submit

data = get_data(day=5, year=2021)
lines = data.splitlines()

grid = [[0 for _ in range(2000)] for _ in range(2000)]

for line in lines:
    a, b = line.split(" -> ")
    x1, y1 = a.split(",")
    x2, y2 = b.split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    if x1 == x2 or y1 == y2:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 1

total = 0

for row in grid:
    for i in row:
        if i >= 2:
            total += 1

    # print()


ans = total
print(ans)

submit(ans, part="a", day=5, year=2021, reopen=False)
