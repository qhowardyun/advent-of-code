from aocd import get_data

data = get_data(day=13, year=2020)
lines = data.splitlines()

startTime = int(lines[0])
busses = list(lines[1].split(","))

ans = 0
minWait = 10 ** 10

for bus in busses:
    if bus != "x":
        bus = int(bus)
        curMinWait = bus - (startTime % bus)
        if curMinWait < minWait:
            ans = curMinWait * bus
print(ans)
