from aocd import get_data, submit

day = 10
data = get_data(day=day, year=2021)
lines = data.splitlines()

stack = []
scores = []
# lines = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "<{([{{}}[<[[[<>{}]]]>[]]",
# ]


def complete(stack):
    lu = {"(": 1, "[": 2, "{": 3, "<": 4}

    points = 0

    for char in stack:
        points *= 5
        points += lu[char]
    return points


inc = []

for line in lines:
    good = True
    for char in line:
        if char in "[({<":
            stack.append(char)
        elif char == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                good = False
                break
        elif char == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                good = False
                break
        elif char == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                good = False
                break
        elif char == ">":
            if stack[-1] == "<":
                stack.pop()
            else:
                good = False
                break

    if good:
        inc.append(line)

for line in inc:
    stack = []
    for char in line:
        if char in "[({<":
            stack.append(char)
        elif char == ")":
            if stack[-1] == "(":
                stack.pop()
        elif char == "]":
            if stack[-1] == "[":
                stack.pop()
        elif char == "}":
            if stack[-1] == "{":
                stack.pop()
        elif char == ">":
            if stack[-1] == "<":
                stack.pop()
    scores.append(complete(reversed(stack)))

ans = sorted(scores)[len(scores) // 2]

print(ans)
submit(ans, part="b", day=day, year=2021, reopen=False)
