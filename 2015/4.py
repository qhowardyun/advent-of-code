from aocd import get_data, submit
import hashlib

data = get_data(day=4, year=2015)
parta = 0
partb = 0

for i in range(10 ** 10):
    code = data + str(i)
    h = int.from_bytes(hashlib.md5(code.encode("utf-8")).digest(), byteorder="big")

    if h < 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFF:
        parta = i

    if h < 0x000000FFFFFFFFFFFFFFFFFFFFFFFFFF:
        partb = i
        break

submit(parta, part="a", day=4, year=2015)
submit(partb, part="b", day=4, year=2015)
