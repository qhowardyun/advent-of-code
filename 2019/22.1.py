from aocd import get_data

data = get_data(day=22, year=2019)

lines = data.splitlines()

SIZE = 119315717514047
pos = 2020

# SIZE = 10
# pos = 9

def icut(pos, N):
    return (pos + N + SIZE) % SIZE

def ideal(pos, N):
    return pow(N, -1, SIZE) * pos % SIZE

def istack(pos):
    return SIZE - 1 - pos

def shuffle(pos):
    for line in reversed(lines):
        if "cut" in line:
            pos = icut(pos, int(line.split()[-1]))
        elif "increment" in line:
            pos = ideal(pos, int(line.split()[-1]))
        elif "stack" in line:
            pos = istack(pos)
        else:
            assert False
    return pos

cycles = 101741582076661

# https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnifwk/
# f(i) = A * i + B

i = 2020
f_i = shuffle(i)
f_f_i = shuffle(f_i)

# Solve for A and B with
# f_i = A * i + B
# f_f_i = A * f_i + B
# f_i - f_f_i = A * (i - f_i)
A = ((f_i - f_f_i) * pow(i - f_i, -1 , SIZE)) % SIZE
B = (f_i - A * i) % SIZE

# composition of linear functions has a closed form
# f(f(f(x))) = A* (A* (A*x + B) + B) + B)
#            = A^3*x + A^2x*B + A*B + B
# f^n(x) = A^n*x + A^(n-1)*B + A^(n-2)*B + ... + B
#        = A^n*x + (A^(n-1) + A^(n-2) + ... + 1) * B
#        = A^n*x + (A^n - 1 / (A - 1) ) * B

A_n_x = pow(A, cycles, SIZE)*i
A_n_1_x = pow(A, cycles, SIZE) - 1
A_1 = A - 1
ans = (A_n_x + (A_n_1_x * pow(A_1, -1, SIZE)) * B) % SIZE
print(ans)
