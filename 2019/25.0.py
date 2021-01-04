import cpu
import itertools

cpu = cpu.CPU("25.state")
cpu.run()

def exec(inp):
    for c in inp:
        cpu.stdin.append(ord(c))
    cpu.stdin.append(ord("\n"))
    cpu.run()
def out():
    out = ""
    while cpu.stdout:
        out += chr(cpu.stdout.pop())
    return out

while True:
    line = input()
    if line == "bf":
        print("brrr")

        possible = ["food ration", "weather machine", "antenna", "space law space brochure", "semiconductor", "planetoid", "monolith"]

        for combo in list(itertools.chain.from_iterable(itertools.combinations(possible, r) for r in range(1, len(possible)+1))):
            print(combo)
            for item in combo:
                exec("drop " + item)
            exec("inv")
            exec("east")
            exec("east")
            exec("west")
            exec("take food ration")
            exec("take weather machine")
            exec("take antenna")
            exec("take space law space brochure")
            exec("take semiconductor")
            exec("take planetoid")
            exec("take monolith")
            bfout = out()
            print(bfout)
            if not "ejected" in bfout:
                break

    elif line == "save":
        open("25.state", "w").write(",".join([str(i) for i in cpu.tape]))
    else:
        for c in line:
            cpu.stdin.append(ord(c))
        cpu.stdin.append(ord("\n"))

    cpu.run()

    while cpu.stdout:
        print(chr(cpu.stdout.pop()), end="")
