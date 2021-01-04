from copy import deepcopy
from aocd import get_data

data = get_data(day=24, year=2019)
gmap = set()

for r, row in enumerate(data.splitlines()):
    for c, char in enumerate(row):
        if char == "#":
            gmap.add((r, c, 0))

for _ in range(200):
    newgmap = set()

    for r in range(0,5):
        for c in range(0,5):
            for d in range(-400, 400):

                count = 0

                # ignore centers
                if r == 2 and c == 2:
                    continue

                # top is center
                if r == 3 and c == 2:
                    for i in range(5):
                        if (4, i, d + 1) in gmap:
                            count += 1
                # normal top
                elif r > 0:
                    if (r - 1, c, d) in gmap:
                        count += 1
                # top is outside
                else:
                    if (1, 2, d - 1) in gmap:
                        count += 1

                # bottom is center
                if r == 1 and c == 2:
                    for i in range(5):
                        if (0, i, d + 1) in gmap:
                            count += 1
                # normal bottom
                elif r < 4:
                    if (r + 1, c, d) in gmap:
                        count += 1
                # bottom is outside
                else:
                    if (3, 2, d - 1) in gmap:
                        count += 1

                # left is center
                if r == 2 and c == 3:
                    for i in range(5):
                        if (i, 4, d + 1) in gmap:
                            count += 1
                # normal left
                elif c > 0:
                    if (r, c - 1, d) in gmap:
                        count += 1
                # left is outside
                else:
                    if (2, 1, d - 1) in gmap:
                        count += 1

                # right is center
                if r == 2 and c == 1:
                    for i in range(5):
                        if (i, 0, d + 1) in gmap:
                            count += 1
                # normal right
                elif c < 4:
                    if (r, c + 1, d) in gmap:
                        count += 1
                # right is outside
                else:
                    if (2, 3, d - 1) in gmap:
                        count += 1

                if (r, c, d) in gmap and count == 1:
                    newgmap.add((r, c, d))
                elif (r, c, d) not in gmap and (count == 1 or count == 2):
                    newgmap.add((r, c, d))

    gmap = deepcopy(newgmap)

print(len(gmap))
