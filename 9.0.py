lines = open("day9.in").read().split()

players = int(lines[0])
rounds = int(lines[6])
current = 3
game = [0, 2, 1, 3]
score = [0 for _ in range(players)]

for i in range(4, rounds + 1):

    #score time
    if i % 23 == 0:
        score[i % players] += i

        remindex = current - 7

        if remindex < 0:
            remindex += len(game) - 1

        #print(remindex)
        #print(game, i, current)

        score[i % players] += game.pop(remindex)
        current -= 7
        #print(game, i, current)
        if current < 0:
            current += len(game)
        continue
    
    if current == 0:
        current += 1
    else:
        current += 2

    current %= len(game)

    if current == 0:
        game.append(i)
    else:
        game.insert(current, i)
    
    #print(game, i, current)

print(max(score))