import math
import itertools
import functools
from aocd import get_data, submit

data = get_data(day=4, year=2020)

lines = data.splitlines()

pp = []
s = ""

for line in lines:
    if line == "":
      pp.append(s)
      s = ""
    else:
        s += " "
        s += line
pp.append(s)
total = 0

for p in pp:
    f = p.split(" ")
    fields = {}
    for d in f:
        if d == "":
            continue
        a, b = d.split(":")
        fields[a] = b
    print(fields)
    print(len(fields.keys()))
    if "byr" in fields.keys():
        v = int(fields["byr"])
        if v > 2002 or v < 1920:
            continue
        if "iyr" in fields.keys():
            v = int(fields["iyr"])
            if v > 2020 or v < 2010:
                continue

            if "eyr" in fields.keys():
                v = int(fields["eyr"])
                if v > 2030 or v < 2020:
                    continue
                if "hgt" in fields.keys():
                    h = int(fields["hgt"][:-2])
                    if fields["hgt"][-1] == "n":
                        if h > 76 or h < 59:
                            continue
                    else:
                        if h > 193 or h < 150:
                            continue

                    if "hcl" in fields.keys():
                        hcl = fields["hcl"]
                        if len(hcl) != 7:
                            continue
                        if hcl[0] != "#":
                            continue
                        for c in hcl[1:]:
                            if c not in ["1","2", "3", "4", "5", "6", "7", "8", "9", "0","a", "b", "c", "d", "e", "f"]:
                                continue
                        if "ecl" in fields.keys():
                            ecl = fields["ecl"]
                            if ecl not in ["amb" ,"blu", "brn","gry","grn","hzl","oth"]:
                                continue
                            if "pid" in fields.keys():
                                pid = fields["pid"]
                                if len(pid) != 9:
                                    continue
                                try:
                                    asda = int(pid)
                                except:
                                    continue
                                print("valid")
                                total += 1

print(total)

# print(pp)

# print(lines)

