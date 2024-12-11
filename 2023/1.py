from typing import Counter
from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache
import re

data = get_data(day=1, year=2023)
# data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """
data = data.replace("one", "one1one")
data = data.replace("two", "two2two")
data = data.replace("three", "three3three")
data = data.replace("four", "four4four")
data = data.replace("five", "five5five")
data = data.replace("six", "six6six")
data = data.replace("seven", "seven7seven")
data = data.replace("eight", "eight8eight")
data = data.replace("nine", "nine9nine")
lines = data.splitlines()

ans = 0

lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

for line in lines:

    match = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line)

    first = lookup[match[0]] * 10
    second = lookup[match[-1]]

    print(line)
    print(first, second)

    line =  first + second
    print(line)
    ans += line
print(ans)



# submit(ans, part="a", day=1, year=2023, reopen=False)
submit(ans, part="b", day=1, year=2023, reopen=False)
