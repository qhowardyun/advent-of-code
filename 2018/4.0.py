lines = open("day4.in").read().splitlines()

lines.sort()
#print("\n".join(lines))

current = 0
sleepStart = 0
times = {}

for line in lines:
    line = line[12:].replace("]", "")
    if "23:" in line:
        line = "00" + line[5:]
    else:
        line = line[3:]
    time = int(line[:2])
    event = line[3:]
    
    if "#" in event:
        current = int(event.split()[1][1:])
        sleepStart = 0
    elif "wakes" in event:
        if not times.__contains__(current):
            times[current] = 0
        times[current] += time - sleepStart
    elif "falls" in event:
        sleepStart = time

guard = list(times.keys())[list(times.values()).index(max(times.values()))]
onDuty = False
sleepStart = 0
mins = [0 for _ in range(61)]

for line in lines:

    line = line[12:].replace("]", "")
    if "23:" in line:
        line = "00" + line[5:]
    else:
        line = line[3:]
    time = int(line[:2])
    event = line[3:]
    
    if "#" + str(guard) in event:
        onDuty = True
    elif "#" in event:
        onDuty = False

    if onDuty:
        if "falls" in event:
            sleepStart = time
        if "wakes" in event:
            for i in range(sleepStart, time):
                mins[i] += 1
maxmin = max(mins)
maxtime = mins.index(maxmin)

print(guard, maxtime)
print(guard * maxtime)