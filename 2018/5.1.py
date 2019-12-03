from __future__ import print_function
import string
line = open("day5.in").read()

def react(text):

    last = ""

    while True:
        for up, low in zip(string.ascii_lowercase, string.ascii_uppercase):
            text = text.replace(up + low, "")
            text = text.replace(low + up, "")

        if last == text:
            return text
        else:
            last = text

smallest = len(line)

for lowChar, upChar in zip(string.ascii_lowercase, string.ascii_uppercase):

    pruned = line.replace(lowChar, "")
    pruned = pruned.replace(upChar, "")
    smallest = min(smallest, len(react(pruned)))

print(smallest)
