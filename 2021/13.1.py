from aocd import get_data, submit

day = 13
data = get_data(day=day, year=2021)

grid = set()

dots, instr = data.split("\n\n")

for d in dots.splitlines():
    x, y = map(int, d.split(","))

    grid.add((x, y))

for line in instr.splitlines():

    f, a, d = line.split()
    ty, val = d.split("=")
    val = int(val)

    newgrid = set()

    for item in grid:
        x, y = item

        if ty == "x":
            newgrid.add((val - abs(val - x), y))
        else:
            newgrid.add((x, val - abs(val - y)))

    grid = newgrid

disp = [[False for _ in range(40)] for _ in range(8)]

for item in grid:
    x, y = item
    disp[y][x] = True

for row in disp:
    for val in row:
        print("X" if val else ".", end="")
    print()
