import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=18, year=2020)
lines = data.splitlines()

def solve(e):
    print("solving:", e)
    if "(" in e:
        start = e.find("(")
        end = 0
        depth = 0
        print("----", start, end)
        for i, c in enumerate(e[start:]):
            if c == ")" and depth == -1:
                print("foud", i, depth)
                end = i + start + 1
                break
            elif c == ")":
                depth += 1
            elif c == "(":
                depth -= 1

        print("++++", start, end)
        return solve(e[:start]  + str(solve(e[start:end][1:-1])) + e[end:])
    elif "*" in e:
        return math.prod(map(solve, e.split(" * ")))
    elif "+" in e:
        return sum(map(solve, e.split(" + ")))
    elif len(e.split()) == 1:
        return int(e)
    else:
        assert False

# print(solve("1 + 2 * 3 + 4 * 5 + 6"))

total = 0

for line in lines:
    total += solve(line)

print(total)
