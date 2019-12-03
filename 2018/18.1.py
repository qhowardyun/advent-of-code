lines = list(map(list, open("18.in").read().splitlines()))

history = []

for i in range(484):
    cpy = [row[:] for row in lines]
    # history.append(lines)

    #print("\n".join([" ".join([a for a in row]) for row in lines]))
    # input()

    #if i % 10 == 0:
        #print(i)

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
    # for index, hist in enumerate(history):
    #    if hist == lines:
    #        print(index, i)
    #        exit()



tree = 0
yard = 0

for row in lines:
    for char in row:
        if char == "#":
            yard += 1
        elif char == "|":
            tree += 1

print(tree, yard, tree * yard)

#6551 loop
#starting 491
#1000000000 % 6551 = 2952
# 491 + 2952 = 3443

#3443 221958
#3442 219387
#3444 223468

#27 loop
#starting 484
#1000000000 % 27 = 1
# 484 + 1 = 485

#485 191151x
#486 193980x
#484 192556x
#
# 
# 190674
# 190164
# 227688