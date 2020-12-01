rows = []
with open('18.in', 'r') as fp:
    for line in fp:
        rows.append(list(line.strip()))

width = len(rows[0])
height = len(rows)

def num_adjacent(x, y):
    empty, tree, lumber = 0, 0, 0
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            my_x = x + i
            my_y = y + j
            if my_x < 0 or my_x >= width or my_y < 0 or my_y >= height:
                continue
            if i == 0 and j == 0: continue
            cell = rows[my_y][my_x]
            if cell == '.':
                empty += 1
            elif cell == '|':
                tree += 1
            else:
                lumber += 1
    return empty, tree, lumber

def process_cell(board, x, y):
    cell = board[y][x]
    empty, tree, lumber = num_adjacent(x, y)
    if cell == ".":
        if tree >= 3:
            return "|"
        else:
            return "."
    elif cell == "|":
        if lumber >= 3:
            return "#"
        else:
            return "|"
    else:
        if lumber >= 1 and tree >= 1:
            return "#"
        else:
            return "."
        
def print_board():
    print( "-")
    for row in rows:
        print("".join(row))

def resource_value(board):
    num = {'.':0,'|':0,'#':0}
    for row in board:
        for col in row:
            num[col] += 1
    return num['|'] * num['#']

table = [202272,
200799,
198489,
197925,
194638,
197736,
198996,
199908,
201142,
204227,
204558,
207080,
208705,
210625,
210420,
213658,
217558,
219906,
222870,
226548,
227897,
226501,
226688,
227688,
226080,
221244,
218272,
211904]
print_board()
for i in range(0, 1000000000):
    new_board = []
    for y in range(0, len(rows)):
        row = rows[y]
        new_board.append(row.copy())
        for x in range(0, len(row)):
            new_board[y][x] = process_cell(rows, x, y)
    rows = new_board
    print(str(i) + " " + str(resource_value(rows)) + " " + str(table[(i - 500) % 28]))
    print(str(table[((1000000000-1) - 500) % 28]))