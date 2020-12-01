from __future__ import print_function

lines = open("day9.in").read().split()

players = int(lines[0])
rounds = int(lines[6])

current = 6
score = [0 for i in range(players)]
game = [0, 4, 2, 1, 3]

def normalize(num):
    global current
    global game

    size = len(game)

    num = num % size

    if num < 0:
        num += size

    return num


for i in range(5, rounds + 1):




    current += 2
    print(current)
    current = normalize(current)

    if i % 23 == 0:
        score[i % players] += i
        popres = game.pop(normalize(current - 9))
        score[i % players] += popres
        current -= 9
        current = normalize(current)
    else:
        if current == 0:
            game.append(i)
            current = len(game) - 1
        else:
            game.insert(current, i)

    print("{:2d} |".format(0), end="")
    for j in game:
        print(" " + str(j), end="")
    print()
    print("     " + (" " * 3 * current) + " ^ " + str(current))


# print(game)

print(max(score))