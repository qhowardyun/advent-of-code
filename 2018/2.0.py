import string

def check3(id):
    for letter in string.ascii_lowercase:
        if id.count(letter) == 3:
            return True
    return False

def check2(id):
    for letter in string.ascii_lowercase:
        if id.count(letter) == 2:
            return True
    return False

c2 = 0
c3 = 0

lines = open("day2.in").read().splitlines()

for line in lines:
    c2 += 1 if check2(line) else 0
    c3 += 1 if check3(line) else 0

print(c2 * c3)