def run(a_in, b_in, next):
    tape = list(map(int, open("7.in").read().strip().split(",")))

    tape.append(0)
    tape.append(0)
    tape.append(0)
    
    inpu = [b_in, a_in]

    ip = 0

    def lookup(i, mode):
        
        if mode == 0:
            return tape[i]
        elif mode == 1:
            return i

    while True:
        
        instruction = tape[ip]

        opcode = instruction % 100
        mode_num = instruction // 100
        modes = []
        
        while mode_num > 0:
            modes.append(mode_num % 10)
            mode_num = mode_num // 10
            
        modes.append(0)
        modes.append(0)
        modes.append(0)
        modes.append(0)
            
        # params
        none = [99]
        single = [3, 4]
        double = [5, 6]
        triple = [1, 2, 7, 8]
        
        increment = 0
        
        a = b = c = 0
        
        ta = tape[ip+1]
        tb = tape[ip+2]
        tc = tape[ip+3]
        
        out = []

        
        if opcode in single:
            a = lookup(tape[ip+1], modes[0])
            increment = 2
        if opcode in double:
            a = lookup(tape[ip+1], modes[0])
            b = lookup(tape[ip+2], modes[1])
            increment = 3
        if opcode in triple:
            a = lookup(tape[ip+1], modes[0])
            b = lookup(tape[ip+2], modes[1])
            c = lookup(tape[ip+3], modes[2])
            increment = 4

        # print("opcode:", opcode)
        # print("tape:", tape)
        # print("modes:", modes)
        # print("a:", a, "b:", b, "c:", c)
        
        if modes[2] == 1:
            print("writing is abs???")
        
        # add
        if opcode == 1:
            tape[tc] = a + b
        # multiply
        elif opcode == 2:
            tape[tc] = a * b
        # input
        elif opcode == 3:
            tape[ta] = inpu.pop()
        # output    
        elif opcode == 4:
            out.append(a)
        # jump if true    
        elif opcode == 5:
            if not a == 0:
                ip = b
                continue
        # jump if false
        elif opcode == 6:
            if a == 0:
                ip = b
                continue
        # less than
        elif opcode == 7:
            if a < b:
                tape[tc] = 1
            else:
                tape[tc] = 0
        # equals
        elif opcode == 8:
            if a == b:
                tape[tc] = 1
            else:
                tape[tc] = 0
            
        # halt    
        elif opcode == 99:
            return out
            break

        ip += increment
        
top = 0
result = []
        
for i in range(5, 10):
    for ii in range(5, 10):
        for iii in range(5, 10):
            for iiii in range(5, 10):
                for iiiii in range(5, 10):
                    value = run(iiiii, run(iiii, run(iii, run(ii, run(i, 0)))))
                    
                    combin = [i, ii, iii, iiii, iiiii]
                    valid = 0 in combin and 1 in combin and 2 in combin and 3 in combin and 4 in combin
                    
                    if value > top and valid:
                        top = value
print(top)