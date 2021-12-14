from aocd import get_data, submit
from collections import Counter, defaultdict

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

np = defaultdict(int)

for i in range(1, len(p)):
    np[p[i - 1] + p[i]] += 1


for _ in range(40):
    newnp = defaultdict(int)
    for k, v in np.items():
        new = d[k]
        newnp[k[0] + new] += v
        newnp[new + k[1]] += v
    np = newnp

f = defaultdict(int)
for k, v in np.items():
    f[k[0]] += v
    f[k[1]] += v
f[p[0]] += 1
f[p[-1]] += 1

a = sorted(f.items(), key=lambda x: x[1])
ans = (a[-1][1] - a[0][1]) // 2

print(ans)
submit(ans, part="b", day=day, year=2021, reopen=False)
