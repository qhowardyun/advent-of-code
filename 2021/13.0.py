from aocd import get_data, submit

day = 13
data = get_data(day=day, year=2021)

grid = set()

dots, instr = data.split("\n\n")

instr = "fold along x=655"

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
        newgrid.add((val - abs(val - x), y))

    grid = newgrid

ans = len(grid)

print(ans)
submit(ans, part="a", day=day, year=2021, reopen=False)
