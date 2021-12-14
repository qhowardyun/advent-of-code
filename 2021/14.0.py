from aocd import get_data, submit
from collections import Counter

day = 14
data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
data = get_data(day=day, year=2021)
p, pairs = data.split("\n\n")
ans = 0

d = {}

for i in pairs.splitlines():
    k, v = i.split(" -> ")
    d[k] = v

for _ in range(10):
    new = ""
    for i in range(1, len(p)):
        new += p[i - 1] + d[p[i - 1] + p[i]]
    new += p[-1]
    p = new


counts = Counter(p)

ans = counts.most_common()[0][1] - counts.most_common()[-1][1]

print(ans)
submit(ans, part="a", day=day, year=2021, reopen=False)
