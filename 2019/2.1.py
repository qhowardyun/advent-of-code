tape = list(map(int, open("2.in").read().strip().split(",")))
fresh_tape = list(tape)

def run(i):
    opcode = tape[i]
    
    if opcode == 99:
        return
    else:
        a = tape[i+1]
        b = tape[i+2]
        r = tape[i+3]
        
        if opcode == 1:
            tape[r] = tape[a] + tape[b]
        if opcode == 2:
            tape[r] = tape[a] * tape[b]
        
        run(i+4)

for i in range(100):
    for j in range(100):
        
        tape = list(fresh_tape)
        
        tape[1] = i
        tape[2] = j

        try:
            run(0)
        except IndexError:
            pass
        
        if tape[0] == 19690720:
            print(i, j)
            exit()