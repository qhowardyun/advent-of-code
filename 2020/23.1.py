from aocd import get_data

data = get_data(day=23, year=2020)

class Node:
    pass

SIZE = 10 ** 6
cups = [int(c) for c in data] + [i for i in range(10, SIZE + 1)]
nodes = [Node() for _ in range(SIZE)]

for i, (n, nex) in enumerate(zip(nodes, nodes[1:] + [nodes[0]])):
    n.val = cups[i]
    n.next = nex

lookup = [-1 for _ in range(SIZE + 1)]
for i, n in enumerate(nodes):
    lookup[n.val] = i

cur = nodes[0]

for _ in range(10 ** 7):
    selected = cur
    three = selected.next
    c1 = three.val
    c2 = three.next.val
    c3 = three.next.next.val
    selected.next = selected.next.next.next.next

    dest = selected.val - 1
    if dest == 0:
        dest = SIZE
    while dest in [c1, c2, c3]:
        dest -= 1
        if dest == 0:
            dest = SIZE
    ins = nodes[lookup[dest]]
    temp = ins.next
    ins.next = three
    three.next.next.next = temp
    cur = selected.next
print(nodes[lookup[1]].next.val * nodes[lookup[1]].next.next.val)
