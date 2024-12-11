from collections import Counter

def get_lex_shift(a):
    shifts = []
    for _ in range(len(a)):
        shifts.append(a)
        a = a[-1] + a[:-1]
    return sorted(shifts)[0]

a = [13, 5604, 31, 2, 13, 4560, 546, 654, 456]

str_a = [str(i) for i in a]
lex_a = [get_lex_shift(i) for i in str_a]

count_a = Counter(lex_a)

total = 0

for value in count_a.values():
    total += value * (value - 1) // 2


print(total)

