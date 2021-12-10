from aocd import get_data, submit

day = 10
data = get_data(day=day, year=2021)
lines = data.splitlines()

ans = 0
stack = []

for line in lines:
    for char in line:
        if char in "[({<":
            stack.append(char)
        elif char == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                ans += 3
                break
        elif char == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                ans += 57
                break
        elif char == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                ans += 1197
                break
        elif char == ">":
            if stack[-1] == "<":
                stack.pop()
            else:
                ans += 25137
                break


print(ans)
submit(ans, part="a", day=day, year=2021, reopen=False)
