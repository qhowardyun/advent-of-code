import cpu

computers = [cpu.CPU("23.in") for _ in range(50)]

# init network
for i, c in enumerate(computers):
    c.stdin.append(i)
    c.run()

# run network
while True:
    for i, c in enumerate(computers):
        if len(c.stdin) == 0:
            c.stdin.append(-1)
        if c.stdout:
            addr = c.stdout.pop()

            if addr == 255:
                c.stdout.pop()
                print(c.stdout.pop())
                exit()
            computers[addr].stdin.append(c.stdout.pop())
            computers[addr].stdin.append(c.stdout.pop())
        c.run()
