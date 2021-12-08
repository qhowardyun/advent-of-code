from aocd import get_data, submit

day = 8
data = get_data(day=day, year=2021)
lines = data.splitlines()

ans = 0

for line in lines:
    output = line.split("|")[-1]
    digits = output.split()
    for d in digits:
        if len(d) in [2, 4, 3, 7]:
            ans += 1

print(ans)
submit(ans, part="a", day=day, year=2021, reopen=False)
