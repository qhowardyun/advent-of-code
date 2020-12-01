import string

lines = open("7.in").read().splitlines()

rules = {i:[] for i in string.ascii_uppercase}

for line in lines:
    req =line[5]
    step = line[36]
    rules[step].append(req)

print(rules)

workers = {}
seconds = 0

while True:

    #find available tasks
    for key, value in rules.items():
        #if no previous steps are required and workers available
        if len(value) == 0 and len(workers) < 5:
            #print("found", key)
            workers[key] = 60 + ord(key) - 65
            rules.pop(key)
            break #start search from beginning
    #find available tasks
    for key, value in rules.items():
        #if no previous steps are required and workers available
        if len(value) == 0 and len(workers) < 5:
            #print("found", key)
            workers[key] = 60 + ord(key) - 65
            rules.pop(key)
            break #start search from beginning
    #find available tasks
    for key, value in rules.items():
        #if no previous steps are required and workers available
        if len(value) == 0 and len(workers) < 5:
            #print("found", key)
            workers[key] = 60 + ord(key) - 65
            rules.pop(key)
            break #start search from beginning
    #find available tasks
    for key, value in rules.items():
        #if no previous steps are required and workers available
        if len(value) == 0 and len(workers) < 5:
            #print("found", key)
            workers[key] = 60 + ord(key) - 65
            rules.pop(key)
            break #start search from beginning
    #find available tasks
    for key, value in rules.items():
        #if no previous steps are required and workers available
        if len(value) == 0 and len(workers) < 5:
            #print("found", key)
            workers[key] = 60 + ord(key) - 65
            rules.pop(key)
            break #start search from beginning
        
    print(seconds, workers)

    #update workers
    if len(workers) == 0:
        break

    seconds += 1
    workerscopy = workers.copy()
    for key, value in workerscopy.items():

            workers[key] = workers[key] - 1
            #worker is done
            if value == 0:
                workers.pop(key)
                rulescopy = rules
                for k, v in rulescopy.items():
                    try:
                        rules[k].remove(key)
                    except:
                        pass

print(seconds)