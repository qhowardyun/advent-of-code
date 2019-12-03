from day4 import d4
from datetime import date, datetime
import string

lines = d4.splitlines()
time = []
event = []

for line in lines:

    date, tim, evt = line.split()
    time.append(datetime.strptime(date + " " + tim, '%Y-%m-%d %H:%M'))
    event.append(evt)

master = sorted(zip(time, event))


guardTime = {}

for i in master:
    if str.isdigit(i[1]):
        guardTime[int(i[1])] = 0


curG = 0
on = False
laston = master[1][0]

#print(laston)

# for line in master:
#     print(line)

# for i in master:
#     tim = i[0]
#     evt = i[1]
#     if str.isdigit(evt):
#         curG = int(evt)
#         laston = tim
#         on = True
#     elif evt == "on":
#         on = True
#         laston = tim
#     elif evt == "off":
#         off = False
#         guardTime[curG] += (tim - laston).seconds / 60

# print(max(guardTime.values()))

right = '2969'
timelist = [0 for _ in range(61)]
printing = False
starttim = []
endtim = []

uplist = []

for i in master:

    if str.isdigit(i[1]):
        printing = False

    if i[1] == right:
        printing = True
    
    if printing:
        uplist.append(i)

print(uplist)
start = -1

# for i in uplist:
#     if str.isdigit(i[1]):
#         start = from day4 import d4
    
from datetime import date, datetime
import string

lines = d4.splitlines()
time = []
event = []

for line in lines:

    date, tim, evt = line.split()
    time.append(datetime.strptime(date + " " + tim, '%Y-%m-%d %H:%M'))
    event.append(evt)

master = sorted(zip(time, event))


guardTime = {}

for i in master:
    if str.isdigit(i[1]):
        guardTime[int(i[1])] = 0


curG = 0
on = False
laston = master[1][0]

#print(laston)

# for line in master:
#     print(line)

# for i in master:
#     tim = i[0]
#     evt = i[1]
#     if str.isdigit(evt):
#         curG = int(evt)
#         laston = tim
#         on = True
#     elif evt == "on":
#         on = True
#         laston = tim
#     elif evt == "off":
#         off = False
#         guardTime[curG] += (tim - laston).seconds / 60

# print(max(guardTime.values()))

right = '2969'
timelist = [0 for _ in range(61)]
printing = False
starttim = []
endtim = []

uplist = []

for i in master:

    if str.isdigit(i[1]):
        printing = False

    if i[1] == right:
        printing = True
    
    if printing:
        uplist.append(i)

start = -1
enable = False

for i in range(0, 59):
    uplist[]

print(timelist)
print(timelist.index(max(timelist)))