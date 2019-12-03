lines = open("day2.in").read()

for line1 in lines.splitlines():
    for line2 in lines.splitlines():
        diff = 0
        for c1, c2 in zip(line1,line2):
            if c1 != c2:
                diff += 1
        if diff == 1:
            print(line1, line2)