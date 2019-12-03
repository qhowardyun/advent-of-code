

def test(regb, instr):

    a = instr[1]
    b = instr[2]
    c = instr[3]

    addr = regb[a] + regb[b]
    addi = regb[a] + b

    mulr = regb[a] * regb[b]
    muli = regb[a] * b

    banr = regb[a] & regb[b]
    bani = regb[a] & b

    borr = regb[a] | regb[b]
    bori = regb[a] | b

    setr = regb[a]
    seti = a

    gtir = 1 if a > regb[b] else 0
    gtri = 1 if regb[a] > b else 0
    gtrr = 1 if regb[a] > regb[b] else 0

    eqir = 1 if a == regb[b] else 0
    eqri = 1 if regb[a] == b else 0
    eqrr = 1 if regb[a] == regb[b] else 0

    instrs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    return instrs

count = 0

lines = open("16p1.in", "r").read().splitlines()
instrlist = [[] for i in range(16)]

for i in range(0, len(lines), 3):
    regb = list(map(int, lines[i][9:-1].split(", ")))
    instr = list(map(int, lines[i + 1].split()))
    rega = list(map(int, lines[i + 2][9:-1].split(", ")))

    
    good = set()
    for index, j in enumerate(test(rega, instr)):
        if j == rega[instr[3]]:
            good.add(index)
    print(instr[0], good)
    instrlist[instr[0]].append(good)

from functools import reduce

for index, i in enumerate(instrlist):
    if len(i) != 0:
        #print(index ,reduce((lambda x, y: x.intersection(y)), i))
        pass
#print(instrlist)
