from aocd import get_data
from collections import deque
from itertools import islice

data = get_data(day=22, year=2020)
p1, p2 = data.split("\n\n")

pi1 = deque(map(int, p1.splitlines()[1:]))
pi2 = deque(map(int, p2.splitlines()[1:]))

gamecount = 0
def recursiveGame(pl1, pl2):
    global gamecount
    gamecount+= 1
    p1 = pl1.copy()
    p2 = pl2.copy()
    paststate = set()
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in paststate:
            return (True, p1)
        paststate.add((tuple(p1), tuple(p2)))

        a = p1.popleft()
        b = p2.popleft()
        if len(p1) >= a and len(p2) >= b:
            newa = deque(islice(list(p1), a))
            newb = deque(islice(list(p2), b))

            if recursiveGame(newa, newb)[0]:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
        else:
            if a > b:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
    if len(p2) == 0:
        return (True, p1)
    else:
        return (False, p2)
p1wins, nums = recursiveGame(pi1, pi2)
print(sum([(i + 1) * x for i, x in enumerate(reversed(nums))]))
