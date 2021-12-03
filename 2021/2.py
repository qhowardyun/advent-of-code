from aocd import get_data, submit

data = get_data(day=2, year=2021)
lines = data.splitlines()

x = 0
depth = 0

for line in lines:
    cmd, val = line.split()
    val = int(val)

    if cmd == "down":
        depth += val
    elif cmd == "up":
        depth -= val
    elif cmd == "forward":
        x += val

ans = x * depth

submit(ans, part="a", day=2, year=2021, reopen=False)

aim = 0
depth = 0
x = 0

for line in lines:
    cmd, val = line.split()
    val = int(val)

    if cmd == "down":
        aim += val
    elif cmd == "up":
        aim -= val
    elif cmd == "forward":
        x += val
        depth += aim * val

ans2 = x * depth

submit(ans2, part="b", day=2, year=2021, reopen=False)
