import cpu

cpu = cpu.CPU("21.in")

PROGRAM = """NOT C T
OR D J
AND T J
NOT A T
OR T J
WALK
"""

for char in PROGRAM:
    cpu.stdin.append(ord(char))

cpu.run()

grid = []
row = []

while len(cpu.stdout) > 0:

    num = cpu.stdout.pop()

    if num > 256:
        print(num)
        exit()

    char = chr(num)

    if char == "\n":
        grid.append(row)
        row = []
    else:
        row.append(char)


print("\n".join(["".join(row) for row in grid]))
