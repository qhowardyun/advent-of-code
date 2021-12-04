from aocd import get_data, submit

data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

data = get_data(day=4, year=2021)
lines = data.split("\n\n")
nums = lines.pop(0)

boards = []
filled = []


def check_done(fill):
    for i in range(5):
        win1 = True
        win2 = True
        for j in range(5):
            win1 = win1 and fill[i * 5 + j]
            win2 = win2 and fill[j * 5 + i]

        if win1 or win2:
            return True
    return False


for board in lines:
    boards.append([])
    filled.append([False for _ in range(25)])
    for line in board.splitlines():
        boards[-1].extend(map(int, line.split()))

drawn = list(map(int, nums.split(",")))


finished = set()


def find_num():
    for num in drawn:
        done = 0
        for b, board in enumerate(boards):
            for n, slot in enumerate(board):
                if num == slot:
                    filled[b][n] = True

            if check_done(filled[b]):
                done += 1

        if done == len(boards):
            last = set(range(len(boards))) - finished
            return list(last)[0], num
        else:
            for b, board in enumerate(boards):
                if check_done(filled[b]):
                    finished.add(b)


last, recent = find_num()

print(last, recent)

winner = boards[last]
winner_fill = filled[last]

total = 0
for i, num in enumerate(winner):
    if not winner_fill[i]:
        total += num

ans = total * recent

print(ans)

submit(ans, part="b", day=4, year=2021, reopen=False)
