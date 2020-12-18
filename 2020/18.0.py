import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=18, year=2020)
lines = data.splitlines()

def solve(e):
    print(e)
    if len(e.split()) == 1:
        return int(e)
    elif e[-1] == ")":
        sep = 0
        depth = 0
        for i, c in enumerate(reversed(e[:-1])):
            if c == "(" and depth == 0:
                # print(len(e) - i - 2)
                sep = len(e) - i - 2
            elif c == ")":
                depth += 1
            elif c == "(":
                depth -= 1

        # print("sep", sep)
        # print(e[:sep])
        # print(e[sep:][1:-1])
        e = e[:sep] + str(solve(e[sep:][1:-1]))
        # print("new e", e)

    # print("split into", e.split())
    if len(e.split()) == 1:
        return int(e)

    if e.split()[-2] == "+":
        return solve(e.split()[-1]) + solve(" ".join(e.split()[:-2]))
    if e.split()[-2] == "*":
        # print(e[-1])
        # print(e[:-4])
        return solve(e.split()[-1]) * solve(" ".join(e.split()[:-2]))

# print(solve("5 + 9 + 5 + 9 * 9"))
# print(solve("5 * (9 * 3 * (6 + 8 + 2 + 5) * 2)"))
# print(solve("4 + (6 + 9) + ((9 * 7 * 5 * 9 * 9 * 8) + 6 + 2 * (7 * 7) * (9 + 7 * 9 + 4))"))

# print(solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))
# print(solve("(5 + (7 + 5 + 8 * 8)) * 2 + 8 + (6 + 5 + 8 + 9 + 3 + (5 * 4 + 8 + 9 + 4)) + 3 * (3 * 5 + 2 + 3 * 7)"))

total = 0

for line in lines:
    total += solve(line)

print(total)
