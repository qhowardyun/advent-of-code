line = [1, 3, 2, 4, 3, 5]
pre = []

tot = 0
for i in line:
    tot += i
    pre.append(tot)
pre.append(0)

print(line)
print(pre)

def sumrange(a, b):
    return pre[b] - pre[a - 1]

print(sumrange(3, 5))
print(sumrange(2, 3))
print(sumrange(3, 3))
print(sumrange(0, 5))