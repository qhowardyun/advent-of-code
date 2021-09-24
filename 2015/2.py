from aocd import get_data, submit

data = get_data(day=2, year=2015)
lines = data.splitlines()

wrapping = 0
ribbon = 0

for line in lines:
    l, w, h = map(int, line.split("x"))
    a = l * w
    b = l * h
    c = w * h
    wrapping += 2 * (a + b + c) + min(a, b, c)
    ribbon += 2 * (l + w + h - max(l, w, h)) + l * w * h

submit(wrapping, part="a", day=2, year=2015)
submit(ribbon, part="b", day=2, year=2015)
