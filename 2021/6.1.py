from aocd import get_data, submit

data = get_data(day=6, year=2021)
lines = data.splitlines()

# lines = ["3,4,3,1,2"]

c = {i: 0 for i in range(9)}

for num in lines[0].split(","):
    c[int(num)] += 1

for _ in range(256):
    spawned = c[0]
    c[0] = c[1]
    c[1] = c[2]
    c[2] = c[3]
    c[3] = c[4]
    c[4] = c[5]
    c[5] = c[6]
    c[6] = c[7] + spawned
    c[7] = c[8]
    c[8] = spawned

ans = 0
for k, v in c.items():
    ans += v

print(ans)
submit(ans, part="b", day=6, year=2021, reopen=False)
