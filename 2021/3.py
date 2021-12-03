from aocd import get_data, submit

data = get_data(day=3, year=2021)
lines = data.splitlines()

count = [0 for _ in range(len(lines[0]))]

for line in lines:
    for i, bit in enumerate(line):
        count[i] += 1 if bit == "1" else 0

gamma = ""
ep = ""

for c in count:
    if c >= len(lines) / 2:
        gamma += "1"
        ep += "0"
    else:
        ep += "1"
        gamma += "0"

print(gamma, ep)

ans = int(gamma, base=2) * int(ep, base=2)

submit(ans, part="a", day=3, year=2021, reopen=False)


most = lines.copy()
least = lines.copy()

for bit in range(len(lines[0])):
    mamt1 = 0
    lamt1 = 0

    for line in most:
        mamt1 += 1 if line[bit] == "1" else 0

    for line in least:
        lamt1 += 1 if line[bit] == "1" else 0

    mamt0 = len(most) - mamt1
    lamt0 = len(least) - lamt1

    if len(most) != 1:
        newmost = []
        target = "1" if mamt1 >= mamt0 else "0"
        for line in most:
            if line[bit] == target:
                newmost.append(line)
        most = newmost

    if len(least) != 1:
        newleast = []
        target = "0" if lamt0 <= lamt1 else "1"
        for line in least:
            if line[bit] == target:
                newleast.append(line)
        least = newleast

    print(bit, most, least)

ls = int(most[0], base=2)
os = int(least[0], base=2)

ans2 = ls * os
submit(ans2, part="b", day=3, year=2021, reopen=False)
