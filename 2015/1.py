from aocd import get_data, submit

data = get_data(day=1, year=2015)

floor = 0

for c in data:
    if c == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
submit(floor, part="a", day=1, year=2015)

floor = 0

for i, c in enumerate(data):
    if c == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        submit(i + 1, part="b", day=1, year=2015)
        break
