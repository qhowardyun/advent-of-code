from aocd import get_data

data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
data = get_data(day=20, year=2020)
lines = data.split("\n\n")

tiles = {}
remaining = set()

for line in lines:
    idx, data = line.split(":")

    idx = int(idx.split()[-1])

    tiles[idx] = data.strip().splitlines()
    remaining.add(idx)

SIZE = 10
def flipV(tile):
    return list(reversed(tile))
def flipH(tile):
    return ["".join(reversed(x)) for x in tile]
def flipB(tile):
    return flipH(flipV(tile))
def r90(tile):
    return ["".join([tile[i][j] for i in range(SIZE - 1, -1, -1)]) for j in range(SIZE)]
def r180(tile):
    return r90(r90(tile))
def r270(tile):
    return r90(r90(r90(tile)))
def ident(tile):
    return tile
def getBorder(tile):
    top = tile[0]
    bottom = tile[-1]
    left = "".join([ x[0] for x in tile])
    right = "".join([ x[-1] for x in tile])
    return (top, right, bottom, left)
def getTile(xy):
    return tiles[layout[xy]]

layout = {}
layout[(15, 15)] = list(tiles.keys()).pop()
remaining.remove(layout[(15,15)])

q = []
q.append((15, 15))

while q:
    xy = q.pop()

    tile = getTile(xy)

    top, right, bottom, left = getBorder(tile)

    for dr, offset, match in [(top, (0, 1), 2),(right, (1, 0), 3),(bottom, (0, -1), 0),(left, (-1, 0), 1)]:
        ex = False
        for k in list(remaining):
            if ex:
                break
            candid = tiles[k]
            for flip in [ident, flipV, flipH, flipB]:
                if ex:
                    break
                for rotate in [ident, r90, r180, r270]:
                    if ex:
                        break
                    if flip == ident and rotate == ident:
                        continue

                    tcandid = rotate(flip(candid))
                    sides = getBorder(tcandid)
                    if sides[match] == dr:
                        nx = xy[0] + offset[0]
                        ny = xy[1] + offset[1]

                        q.append((nx, ny))
                        tiles[k] = tcandid
                        remaining.remove(k)
                        layout[(nx, ny)] = k
                        ex = True
                        break

minx = 999999
maxx = 0
miny = 999999
maxy = 0

for x, y in layout.keys():
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

print(layout[(minx, miny)] * layout[(minx, maxy)] * layout[(maxx, miny)] * layout[(maxx, maxy)])

def chopBorders(tile):
    tile.pop(0)
    tile.pop()
    return [x[1:-1] for x in tile]

IMGSIZE = 8 * (maxx - minx + 1)
image = [["a" for _ in range(IMGSIZE)] for _ in range(IMGSIZE)]

for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        tile = chopBorders(tiles[layout[(x, y)]])
        xoff = (x - minx) * 8 + 0
        yoff = ((maxy - miny) - (y - miny)) * 8 + 0
        for i, line in enumerate(tile):
            for j, c in enumerate(line):
                xidx = xoff + j
                yidx = yoff + i
                image[yidx][xidx] = c

def r90i(tile):
    return ["".join([tile[i][j] for i in range(IMGSIZE - 1, -1, -1)]) for j in range(IMGSIZE)]

# find monster
monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

mx = len(monster[0])
my = len(monster)

def searchMonster(r, c):
    for dr, row in enumerate(monster):
        for dc, char in enumerate(row):
            if char == "#":
                if image[r + dr][c + dc][0] != "#":
                    return False
    return True

def countMonster(r, c):
    total = 0
    for dr, row in enumerate(monster):
        for dc, char in enumerate(row):
            if image[r + dr][c + dc][0] == "#":
                total += 1
    return total - 15

image = flipH(image)
image = r90i(image)

monsters = 0
for r in range(len(image) - my + 1):
    for c in range(len(image[r]) - mx + 1):
        if searchMonster(r, c):
            monsters += 1
total = 0
for row in image:
    for c in row:
        if c == "#":
            total += 1
print(total - 15 * monsters)
