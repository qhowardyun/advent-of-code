from aocd import get_data, submit
from collections import defaultdict, Counter
from functools import lru_cache

day = 19
data = get_data(day=day, year=2021)


@lru_cache
def trans(p, t):
    assert 0 <= t <= 47

    x = p[0] * (1 if t % 2 == 0 else -1)
    y = p[1] * (1 if t % 4 <= 1 else -1)
    z = p[2] * (1 if t % 8 <= 3 else -1)

    if t // 8 == 0:
        return (x, y, z)
    elif t // 8 == 1:
        return (x, z, y)
    elif t // 8 == 2:
        return (y, z, x)
    elif t // 8 == 3:
        return (y, x, z)
    elif t // 8 == 4:
        return (z, x, y)
    else:
        return (z, y, x)


scanners = data.split("\n\n")
beacons = []

for scanner in scanners:
    beacon_list = []
    for i, line in enumerate(scanner.splitlines()[1:]):
        a, t, c = list(map(int, line.split(",")))
        beacon_list.append((a, t, c))
    beacons.append(beacon_list)


transform = [None for _ in range(len(beacons))]
transform[0] = (0, 0, 0)
done = set([0])
todo = set(range(1, len(beacons)))
done_points = set(beacons[0])


while todo:
    matched = None
    for t in todo:
        if matched:
            continue
        for trans_test in range(48):
            counts = defaultdict(int)
            for bp in beacons[t]:
                for dp in done_points:
                    bpt = trans(bp, trans_test)
                    dx = -bpt[0] + dp[0]
                    dy = -bpt[1] + dp[1]
                    dz = -bpt[2] + dp[2]
                    counts[(dx, dy, dz)] += 1

            for k, v in counts.items():
                if v >= 12:
                    transform[t] = (k[0], k[1], k[2])
                    for bp in beacons[t]:
                        bpt = trans(bp, trans_test)
                        done_points.add((bpt[0] + k[0], bpt[1] + k[1], bpt[2] + k[2]))
                    matched = t
    todo.remove(matched)
    done.add(matched)
    print("todo:", todo)

ans1 = len(done_points)
print(ans1)
submit(ans1, part="a", day=day, year=2021, reopen=False)

ans2 = 0

for p1 in transform:
    for p2 in transform:
        ans2 = max(ans2, abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]))

print(ans2)
submit(ans2, part="b", day=day, year=2021, reopen=False)
