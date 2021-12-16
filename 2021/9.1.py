from aocd import get_data, submit
from collections import defaultdict

day = 9
data = """2199943210
3987894921
9856789892
8767896789
9899965678"""
data = get_data(day=day, year=2021)
grid = [[int(c) for c in line] for line in data.splitlines()]

ans = 0
lowest = set()


for r in range(len(grid)):
    for c in range(len(grid[r])):
        d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        good = True
        for dx, dy in d:
            nx = dx + r
            ny = dy + c

            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[r])):
                if grid[r][c] >= grid[nx][ny]:
                    good = False
                    break

        if good:
            lowest.add((r, c))


def find_lowest(r, c, seen=None):

    if grid[r][c] == 9:
        return

    if not seen:
        seen = set()

    if (r, c) in lowest:
        return (r, c)
    else:
        smallest = 9
        idx = -1
        d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i, (dx, dy) in enumerate(d):
            nx = dx + r
            ny = dy + c
            if (
                (nx, ny) not in seen
                and (0 <= nx < len(grid))
                and (0 <= ny < len(grid[r]))
            ):
                if smallest > grid[nx][ny]:
                    smallest = grid[nx][ny]
                    idx = i
        if idx == -1:
            0 / 0
        seen.add((r, c))
        return find_lowest(r + d[idx][0], c + d[idx][1], seen)


b = defaultdict(int)

for r in range(len(grid)):
    for c in range(len(grid[r])):
        root = find_lowest(r, c, set())
        if root:
            b[root] += 1

top = sorted([i for i in b.values()])
ans2 = top[-1] * top[-2] * top[-3]
print(ans2)
submit(ans2, part="b", day=day, year=2021, reopen=False)
