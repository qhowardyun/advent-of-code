import cpu

computers = [cpu.CPU("23.in") for _ in range(50)]

# init network
for i, c in enumerate(computers):
    c.stdin.append(i)
    c.run()

NATX = -1
NATY = -1
LAST = -2

# run network
while True:
    empty = 0
    for i, c in enumerate(computers):
        if len(c.stdin) == 0:
            c.stdin.append(-1)
            empty += 1
        if c.stdout:
            addr = c.stdout.pop()
            X = c.stdout.pop()
            Y = c.stdout.pop()
            if addr == 255:
                NATX = X
                NATY = Y
            else:
                computers[addr].stdin.append(X)
                computers[addr].stdin.append(Y)
        c.run()
    if empty == 50 and NATY != -1:
        if NATY == LAST:
            print(NATY)
            exit()
        else:
            LAST = NATY
        computers[0].stdin.append(NATX)
        computers[0].stdin.append(NATY)

