from aocd import get_data

import cpu

total = 0

for x in range(50):
    for y in range(50):
        program = cpu.CPU("19.in")
        program.stdin.append(x)
        program.stdin.append(y)
        program.run()
        if program.stdout.pop() == 1:
            total += 1
print(total)
