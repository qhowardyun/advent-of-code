from __future__ import print_function
import string
line = open("day5.in").read()

last = ""
done = False

while not done:
    for up, low in zip(string.ascii_lowercase, string.ascii_uppercase):
        line = line.replace(up + low, "")
        line = line.replace(low + up, "")
    
    if last == line:
        done = True
    else:
        last = line

print(line)
print(len(line))
