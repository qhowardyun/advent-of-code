from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 12
data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
data = get_data(day=day, year=2021)
lines = data.splitlines()
ans = 0

G = defaultdict(list)

for line in lines:
    a, b = line.split("-")
    G[a].append(b)
    G[b].append(a)


q = [("start", ["start"])]
paths = []

while q:
    cur, path = q.pop()

    for neighbour in G[cur]:
        if neighbour == "end":
            path.append("end")
            paths.append(path)
        elif neighbour == neighbour.lower():
            if neighbour in path:
                continue
            else:
                q.append((neighbour, path + [neighbour]))
        else:
            q.append((neighbour, path + [neighbour]))

ans = len(paths)
submit(ans, part="a", day=day, year=2021, reopen=False)
