from aocd import get_data, submit

day = 9
data = get_data(day=day, year=2021)
# data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""
grid = [[c for c in line] for line in data.splitlines()]

ans = 0

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
            ans += int(grid[r][c]) + 1


print(ans)
submit(ans, part="a", day=day, year=2021, reopen=False)
