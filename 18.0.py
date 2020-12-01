lines = list(map(list, open("18.in").read().splitlines()))

for i in range(10):
    cpy = [row[:] for row in lines]

    for x in range(1, 51):
        for y in range(1, 51):

            tree = 0
            yard = 0

            if lines[x + 1][y+ 1] == "|":
                tree += 1
            elif lines[x + 1][y+ 1] == "#":
                yard += 1

            if lines[x][y + 1] == "|":
                tree += 1
            elif lines[x][y + 1] == "#":
                yard += 1

            if lines[x - 1][y + 1] == "|":
                tree += 1
            elif lines[x - 1][y + 1] == "#":
                yard += 1

            if lines[x + 1][y] == "|":
                tree += 1
            elif lines[x + 1][y] == "#":
                yard += 1

            if lines[x - 1][y] == "|":
                tree += 1
            elif lines[x - 1][y] == "#":
                yard += 1

            if lines[x + 1][y - 1] == "|":
                tree += 1
            elif lines[x + 1][y - 1] == "#":
                yard += 1

            if lines[x][y - 1] == "|":
                tree += 1
            elif lines[x][y - 1] == "#":
                yard += 1

            if lines[x - 1][y - 1] == "|":
                tree += 1
            elif lines[x - 1][y - 1] == "#":
                yard += 1
            
            cur = lines[x][y]

            if cur == ".":
                if tree >= 3:
                    cpy[x][y] = "|"
            elif cur == "|":
                if yard >= 3:
                    cpy[x][y] = "#"
            elif cur == "#":
                if not (yard >= 1 and tree >= 1):
                    cpy[x][y] = "."
    
    lines = cpy

tree = 0
yard = 0

for row in lines:
    for char in row:
        if char == "#":
            yard += 1
        elif char == "|":
            tree += 1

print(tree, yard, tree * yard)
