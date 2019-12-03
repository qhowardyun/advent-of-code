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

    if "falls" in event:
        sleepStart = time
    if "wakes" in event:
        if not times.__contains__(current):
            times[current] = [0 for _ in range(61)]
        for i in range(sleepStart, time):
            times[current][i] += 1

maxmin = 0
maxid = 0
for key, value in times.items():
    #print(key, end = ":")
    #print(" ".join(map(str, value)))
    for i in value:
        if i > maxmin:
            maxmin = i
            maxid = key

maxindex = times[maxid].index(maxmin)

print(maxid, maxindex)
print(maxid * maxindex)
