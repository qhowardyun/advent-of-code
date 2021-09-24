from aocd import get_data, submit

data = get_data(day=5, year=2015)
lines = data.splitlines()

nice = 0

for line in lines:

    # matching pairs
    pairs = set()
    bad = True
    to_add = None
    for i in range(len(line) - 1):
        pair = line[i] + line[i + 1]
        if pair in pairs:
            bad = False
            break
        else:
            if to_add:
                pairs.add(to_add)
            to_add = pair
    if bad:
        continue

    # letter inbetween
    copy = "  " + line
    bad = True
    for a, b in zip(copy, line):
        if a == b:
            bad = False
            break
    if bad:
        continue

    nice += 1

print(nice)
submit(nice, part="b", day=5, year=2015)
