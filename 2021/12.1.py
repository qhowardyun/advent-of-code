from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 12
data = get_data(day=day, year=2021)
lines = data.splitlines()
ans = 0

G = defaultdict(list)

for line in lines:
    a, b = line.split("-")
    G[a].append(b)
    G[b].append(a)


q = [("start", ["start"], False)]
paths = []

while q:
    cur, path, doubled = q.pop()

    for neighbour in G[cur]:
        if neighbour == "end":
            path.append("end")
            paths.append(path)
        elif neighbour == "start":
            continue
        elif neighbour == neighbour.lower():
            if path.count(neighbour) == 0:
                q.append((neighbour, path + [neighbour], doubled))
            elif path.count(neighbour) == 1 and not doubled:
                q.append((neighbour, path + [neighbour], True))
            else:
                continue
        else:
            q.append((neighbour, path + [neighbour], doubled))

ans = len(paths)
submit(ans, part="b", day=day, year=2021, reopen=False)
