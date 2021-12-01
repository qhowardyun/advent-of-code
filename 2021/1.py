from aocd import get_data, submit

data = get_data(day=1, year=2021)
lines = list(map(int, data.splitlines()))
# lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

prev = lines[0]
total = 0

for val in lines:
    if val > prev:
        total += 1
    prev = val

print(total)

submit(total, part="a", day=1, year=2021)


p2 = 0
for i, val in enumerate(lines):
    if i + 4 > len(lines):
        continue
    if lines[i] < lines[i + 3]:
        p2 += 1

print(p2)
submit(p2, part="b", day=1, year=2021)
