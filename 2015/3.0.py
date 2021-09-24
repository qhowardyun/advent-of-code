from aocd import get_data, submit

data = get_data(day=3, year=2015)


dx = {">": 1, "<": -1, "^": 0, "v": 0}
dy = {">": 0, "<": 0, "^": 1, "v": -1}

houses = set([(0, 0)])
x = 0
y = 0

for c in data:
    x += dx[c]
    y += dy[c]
    houses.add((x, y))

submit(len(houses), part="a", day=3, year=2015)
