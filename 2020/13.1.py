from aocd import get_data
from functools import reduce
data = get_data(day=13, year=2020)
lines = data.splitlines()

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

def chinese_remainder(n, a):
    _sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

busses = list(lines[1].split(","))
product = reduce(lambda a, b: a * b, [int(x) if x != "x" else 1 for x in busses])

A = []
B = []
for i, bus in enumerate(busses):
    if bus != "x":
        A.append(int(bus))
        B.append(i)

print(product - chinese_remainder(A, B))
