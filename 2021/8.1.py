from aocd import get_data, submit
from collections import defaultdict

day = 8
data = get_data(day=day, year=2021)
lines = data.splitlines()

ans2 = 0


def ident(digits):
    m = defaultdict(list)
    f = defaultdict(list)

    for d in digits:
        m[len(d)].append(d)

        if len(d) == 2:
            f[1] = d
        elif len(d) == 3:
            f[7] = d
        elif len(d) == 4:
            f[4] = d
        elif len(d) == 7:
            f[8] = d

    # find 3 using 1
    for x in m[5]:
        if f[1][0] in x and f[1][1] in x:
            f[3] = x
            m[5].remove(x)
            break

    # 4 - 7 (left top and middle options)
    ltmopts = list(set(m[4][0]) - set(m[3][0]))
    # find 5 using ltmopts
    for x in m[5]:
        if ltmopts[0] in x and ltmopts[1] in x:
            f[5] = x
            m[5].remove(x)
            break

    # find 2 using elimination
    f[2] = m[5].pop()

    # find 9 using 5 + 1
    nine = set(f[5] + f[1])
    for x in m[6]:
        if set(x) == set(nine):
            f[9] = x
            m[6].remove(x)
            break

    # find 0 using 1
    for x in m[6]:
        if f[1][0] in x and f[1][1] in x:
            f[0] = x
            m[6].remove(x)
            break

    # find 2 using elimination
    f[6] = m[6].pop()

    return f


total = 0
for line in lines:
    data, q = line.split("|")
    key = ident(data.split())

    num = ""

    for d in q.split():
        for k, v in key.items():
            if set(d) == set(v):
                num += str(k)

    total += int(num)


submit(total, part="b", day=day, year=2021, reopen=False)
