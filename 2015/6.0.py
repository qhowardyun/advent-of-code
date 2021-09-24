from aocd import get_data, submit

data = get_data(day=6, year=2015)
lines = data.splitlines()

grid = [[False for _ in range(1000)] for _ in range(1000)]

for line in lines:
    parts = line.split()
    x1, y1 = map(int, parts[-3].split(","))
    x2, y2 = map(int, parts[-1].split(","))

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if parts[0] == "toggle":
                grid[i][j] = not grid[i][j]
            elif parts[1] == "on":
                grid[i][j] = True
            elif parts[1] == "off":
                grid[i][j] = False

on = 0
for row in grid:
    for cell in row:
        if cell:
            on += 1

print(on)
submit(on, part="a", day=6, year=2015)
