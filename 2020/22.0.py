from aocd import get_data
from collections import deque

data = get_data(day=22, year=2020)
p1, p2 = data.split("\n\n")

p1 = deque(map(int, p1.splitlines()[1:]))
p2 = deque(map(int, p2.splitlines()[1:]))

while p1 and p2:
    a = p1.popleft()
    b = p2.popleft()

    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)

print(sum([(i + 1) * x for i, x in enumerate(reversed(p2))]))
