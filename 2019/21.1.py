import cpu

cpu = cpu.CPU("21.in")

PROGRAM = """NOT B J
NOT C T
OR T J
AND D J
AND H J
NOT A T
OR T J
RUN
"""

# ###.#...#.#.##
# ^   ^   ^
# #####.#.#..##.###
#     ^   ^   ^

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
