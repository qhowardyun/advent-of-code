from aocd import get_data, submit

data = get_data(day=7, year=2021)
lines = data.splitlines()
nums = list(map(int, lines[0].split(",")))

ans = 10 ** 10
for i in range(max(nums)):
    cur = 0
    for num in nums:
        cur += abs(i - num)
    ans = min(ans, cur)

ans2 = 10 ** 10
for i in range(max(nums)):
    cur = 0
    for num in nums:
        dist = abs(i - num)
        cur += int((1 + dist) * 0.5 * dist)
    ans2 = min(ans2, cur)

print(ans, ans2)
submit(ans, part="a", day=7, year=2021, reopen=False)
submit(ans2, part="b", day=7, year=2021, reopen=False)
