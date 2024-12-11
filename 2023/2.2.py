
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import re

day = 2
data = get_data(day=day, year=2023)

lines = data.splitlines()
# lines = [int(x) for x in lines]
ans = 0
# Game 11: 3 red, 3 blue, 9 green; 3 green, 4 red, 8 blue; 1 red, 12 blue; 2 red, 5 blue, 7 green; 11 blue, 2 red, 6 green

for line in lines:
    game, rounds = line.split(":")
    id = int(re.findall(r"\d+", game)[0])

    red, green, blue = 0, 0, 0

    for round in  rounds.split(";"):
        try:
            v = int(re.search(r"(\d+) red", round).group(1))
            red = max(v, red)
        except:
            pass


        try:
            v = int(re.search(r"(\d+) green", round).group(1))
            green = max(v, green)
        except:
            pass

        try:
            v = int(re.search(r"(\d+) blue", round).group(1))
            blue = max(v, blue)
        except Exception as e:
            pass

    ans += red * green * blue


print(ans)
# submit(ans, part="a", day=day, year=2023, reopen=False)
submit(ans, part="b", day=day, year=2023, reopen=False)
