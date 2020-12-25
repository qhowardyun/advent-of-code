from aocd import get_data

data = get_data(day=25, year=2020)
lines = data.splitlines()

pubd = int(lines[0])
pubk = int(lines[1])

i = 7
counta = 1
while i != pubd:
    i *= 7
    i %= 20201227
    counta += 1
print(counta)

i = 7
countb = 1
while i != pubk:
    i *= 7
    i %= 20201227
    countb += 1

print(countb)

transd = 1
for _ in range(countb):
    transd *= pubd
    transd %= 20201227

transk = 1
for _ in range(counta):
    transk *= pubk
    transk %= 20201227

print(transd, transk)
