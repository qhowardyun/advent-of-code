from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 21
data = get_data(day=day, year=2021)
lines = data.splitlines()
p1 = int(lines[0].split()[-1])
p2 = int(lines[1].split()[-1])

dp = defaultdict(int)
dp[(0, 0, p1, p2, 0)] = 1

p1w = 0
p2w = 0

for score1 in range(21):
    for score2 in range(21):
        for pos1 in range(1, 11):
            for pos2 in range(1, 11):
                cur_state = (score1, score2, pos1, pos2, 0)
                cur_count = dp[cur_state]
                for roll, copies in {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}.items():
                    newpos = (pos1 + roll - 1) % 10 + 1
                    newscore = score1 + newpos
                    if newscore >= 21:
                        p1w += cur_count * copies
                    else:
                        dp[(newscore, score2, newpos, pos2, 1)] += cur_count * copies
                cur_state = (score1, score2, pos1, pos2, 1)
                cur_count = dp[cur_state]
                for roll, copies in {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}.items():
                    newpos = (pos2 + roll - 1) % 10 + 1
                    newscore = score2 + newpos
                    if newscore >= 21:
                        p2w += cur_count * copies
                    else:
                        dp[(score1, newscore, pos1, newpos, 0)] += cur_count * copies


print(p1w, p2w)
submit(max(p1w, p2w), part="b", day=day, year=2021, reopen=False)
