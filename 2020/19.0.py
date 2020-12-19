import re
from functools import lru_cache

from aocd import get_data

data = get_data(day=19, year=2020)
rules, lines = data.split("\n\n")
rules = rules.splitlines()

r = {}

for rule in rules:
    idx, ru = rule.split(": ")

    parts = ru.split()
    if '"' in ru:
        r[idx] = ["L", ru[1]]
    elif '|' in ru:
        a, b = ru.split("|")
        r[idx] = ["|", a.split(), b.split()]
    else:
        r[idx] = ["C", ru.split()]


@lru_cache()
def genR(id):

    rule = r[id]

    if rule[0] == "C":
        return "(" + "".join(map(genR, rule[1])) + ")"
    elif rule[0] == "|":
        return "((" + "".join(map(genR, rule[1])) + ")|(" + "".join(map(genR, rule[2])) + "))"
    elif rule[0] == "L":
        return rule[1]

regS = "^" + genR("0") + "$"
total = 0

for line in lines.splitlines():
    if re.match(regS, line):
        total += 1
print(total)

