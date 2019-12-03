data = list(map(int, open("day8.in").read().split()))
#data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


def eat(data):
    n, m = data.pop(0), data.pop(0)
    #print("Nodes {} Metas {}".format(n, m))

    total = []
    returntotal = 0

    if n == 0:
        #print("Returning {} Sum {}".format(data[m:], sum(data[:m])))
        return data[m:], sum(data[:m])

    for _ in range(n):
        #print("Starting node {}".format(data))
        data, add = eat(data)
        total.append(add)

    #print("Adding to sum {}".format(data[:m]))
    for i in data[:m]:
        try:
            returntotal += total[i - 1]
        except:
            pass

    return data[m:], returntotal


print(eat(data))