from aocd import get_data

data = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
data = get_data(day=24, year=2020)
lines = data.splitlines()

grid = [[True for _ in range(1000)] for _ in range(1000)]


for line in lines:
    curx, cury = 500, 500
    up = False
    down = False
    dx, dy = 0, 0
    offset = False
    for c in line:
        if up and c == "e":
            if not offset:
                dx += 1
            dy += 1
            up = False
            offset = not offset
        elif up and c == "w":
            if offset:
                dx -= 1
            dy += 1
            up = False
            offset = not offset
        elif down and c == "e":
            if not offset:
                dx += 1
            dy += -1
            down = False
            offset = not offset
        elif down and c == "w":
            if offset:
                dx -= 1
            dy += -1
            down = False
            offset = not offset
        elif c == "s":
            down = True
        elif c == "n":
            up = True
        elif c == "e":
            dx += 1
        elif c == "w":
            dx += -1
        else:
            assert False
    newx, newy = curx + dx, cury + dy
    grid[newx][newy] = not grid[newx][newy]

total = 0
for row in grid:
    for c in row:
        if not c:
            total += 1
print(total)


