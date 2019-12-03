l1 = set()

l1.add(5)
l1.add(6)
l1.add(14)

#print(6 in l1)

from datetime import date, datetime

print(datetime.strptime("1518-09-24 00:12", '%Y-%m-%d %H:%M'))

a = "aoeaoe"
b = "oeoe"

print(a, b, a == b)

a.replace("a", "")

print(a, b, a == b)

def texta(text):
    text = text.replace("a", "")
    print(text)
    return text

print(texta("aaoea"))

from collections import deque

dq = deque(['b','c','d'])
print(dq)

# adding an element to the right of the queue
dq.append('e')
print(dq)

# adding an element to the left of the queue
dq.appendleft('a')
print(dq)

# iterate over deque's elements
for elt in dq:
    print(elt)

# pop out an element at from the right of the queue
dq.pop()
print(dq)

# pop out an element at from the right of the queue
dq.popleft()
print(dq)

# print as list
print(list(dq))

# reversed list
print(list(reversed(dq)))

# empty the deque element
dq.clear()
