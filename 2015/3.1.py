from aocd import get_data, submit

data = get_data(day=3, year=2015)


dx = {">": 1, "<": -1, "^": 0, "v": 0}
dy = {">": 0, "<": 0, "^": 1, "v": -1}

houses = set([(0, 0)])
x = 0
y = 0
x2 = 0
y2 = 0
robo = False

for c in data:
    if robo:
        x2 += dx[c]
        y2 += dy[c]
        houses.add((x2, y2))
    else:
        x += dx[c]
        y += dy[c]
        houses.add((x, y))
    robo = not robo

submit(len(houses), part="b", day=3, year=2015)
