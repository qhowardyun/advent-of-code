import string

lines = open("day7.in").read().splitlines()

rules = {i:[] for i in string.ascii_uppercase}

for line in lines:
    req =line[5]
    step = line[36]
    rules[step].append(req)

#print(rules)

output = ""

while len(rules) > 0:
    for key, value in rules.items():
        if len(value) == 0:
            output += key

            for k, v in rules.items():
                    try:
                        rules[k].remove(key)
                    except:
                        pass
            rules.pop(key)
            #print(rules)
            break

print(output)