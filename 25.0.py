lines = open("25.in").read().splitlines()

nums = []

for line in lines:
    nums.append(map(int, line.split(',')))

graph = [set() for i in range(len(lines))]

for index, i in enumerate(lines):
    for gin, g in enumerate(lines):
        dist = 0
        dist += abs(nums[index][0] - nums[gin][0])
        dist += abs(nums[index][1] - nums[gin][1])
        dist += abs(nums[index][2] - nums[gin][2])
        dist += abs(nums[index][3] - nums[gin][3])
        
        if dist <= 3 and i != g:
            graph[index].add(gin) 
            graph[gin].add(index)

done = set()
count = 0

for index, i in enumerate(graph):
    if not index in done:
        stack = list(i)
        doned = set()

        while len(stack) > 0:
            cur = stack.pop()
            if not cur in doned:
                stack.extend(list(graph[cur]))
            doned.add(cur)
            done.add(cur)

        count += 1

print(count)