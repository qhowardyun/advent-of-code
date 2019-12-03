tape = list(map(int, open("2.in").read().strip().split(",")))

# restore error code
tape[1] = 12
tape[2] = 2

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

run(0)
print(tape[0])