from aocd import get_data

data = get_data(day=22, year=2019)
data = """cut 6
deal with increment 7
deal into new stack
"""


lines = data.splitlines()

SIZE = 10007
SIZE = 10
cards = [i for i in range(SIZE)]

def cut(cards, N):
    return cards[N:] + cards[:N]

def deal(cards, N):
    pos = 0
    newcards = [0 for _ in range(SIZE)]

    for c in cards:
        newcards[pos] = c
        pos += N
        pos %= SIZE
    return newcards

for line in lines:
    if "cut" in line:
        cards = cut(cards, int(line.split()[-1]))
    elif "increment" in line:
        cards = deal(cards, int(line.split()[-1]))
    elif "stack" in line:
        cards = list(reversed(cards))
    else:
        assert False
    print(cards)

print(cards.index(2019))
