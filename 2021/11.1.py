from aocd import get_data, submit

day = 11
data = """11111
19991
19191
19991
11111"""
data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
data = get_data(day=day, year=2021)

ngrid = {}

grid = list(map(list, data.splitlines()))
for x, row in enumerate(grid):
    for y, c in enumerate(row):
        ngrid[(x, y)] = int(c)


def pgrid(ngrid):
    grid = [[0 for _ in range(5)] for _ in range(5)]

    for (x, y), v in ngrid.items():
        grid[x][y] = v

    for row in grid:
        for c in row:
            print(c, end="")
        print()

    print("-" * 10)


for ans in range(100000):
    q = []
    seen = set()
    for k in ngrid.keys():
        ngrid[k] += 1
        if ngrid[k] > 9:
            q.append(k)

    while q:
        x, y = q.pop()
        if (x, y) in seen:
            continue
        else:
            seen.add((x, y))

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not (dx == 0 and dy == 0):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx <= 9 and 0 <= ny <= 9:
                        ngrid[(nx, ny)] += 1
                        if ngrid[(nx, ny)] > 9:
                            q.append((nx, ny))

    for s in seen:
        ngrid[s] = 0
    if len(seen) == 100:
        print(ans + 1)
        submit(ans + 1, part="b", day=day, year=2021, reopen=False)
        exit()
