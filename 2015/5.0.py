from aocd import get_data, submit

data = get_data(day=5, year=2015)
lines = data.splitlines()

nice = 0

for line in lines:

    vcount = 0
    for v in "aeiou":
        vcount += line.count(v)
    if vcount < 3:
        continue

    copy = " " + line
    bad = True
    for a, b in zip(copy, line):
        if a == b:
            bad = False
            break
    if bad:
        continue

    bad = False

    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in line:
            bad = True
            break

    if bad:
        continue

    nice += 1

print(nice)
submit(nice, part="a", day=5, year=2015)
