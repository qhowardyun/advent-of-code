from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 21
data = get_data(day=day, year=2021)
lines = data.splitlines()
ans = 0

dcur = 0
dcount = 0


def roll():
    global dcount
    global dcur
    dcount += 1
    dcur += 1
    if dcur == 101:
        dcur = 1
    return dcur


p1 = int(lines[0].split()[-1])
p2 = int(lines[1].split()[-1])
scores = [0, 0]
positions = [p1, p2]

turn = 0

while True:
    moves = roll() + roll() + roll()
    positions[turn] = (positions[turn] + moves - 1) % 10 + 1
    scores[turn] += positions[turn]

    if scores[turn] >= 1000:
        break

    turn = 1 if turn == 0 else 0


ans = dcount * scores[1 if turn == 0 else 0]
print(ans)
submit(ans, part="a", day=day, year=2021, reopen=False)
