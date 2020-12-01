class cpu:
    
    def __init__(self):
        
        self.tape = list(map(int, open("7.in").read().strip().split(",")))
        self.tape.append(0)
        self.tape.append(0)
        self.tape.append(0)
        self.out = 0

        self.ip = 0

    def lookup(self, i, mode):
        
        if mode == 0:
            return self.tape[i]
        elif mode == 1:
            return i
        
    def inpu(self, val):
        
        if self.state == "halt":
            raise Exception("nope")
        
        self.tape[self.ta] = val
        self.run()
        

    def run(self):
        
        while True:
            instruction = self.tape[self.ip]

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
            
            ta = self.tape[self.ip+1]
            tb = self.tape[self.ip+2]
            tc = self.tape[self.ip+3]

            
            if opcode in single:
                a = self.lookup(self.tape[self.ip+1], modes[0])
                increment = 2
            if opcode in double:
                a = self.lookup(self.tape[self.ip+1], modes[0])
                b = self.lookup(self.tape[self.ip+2], modes[1])
                increment = 3
            if opcode in triple:
                a = self.lookup(self.tape[self.ip+1], modes[0])
                b = self.lookup(self.tape[self.ip+2], modes[1])
                c = self.lookup(self.tape[self.ip+3], modes[2])
                increment = 4

            # print("opcode:", opcode)
            # print("tape:", tape)
            # print("modes:", modes)
            # print("a:", a, "b:", b, "c:", c)
            
            # add
            if opcode == 1:
                self.tape[tc] = a + b
            # multiply
            elif opcode == 2:
                self.tape[tc] = a * b
            # input
            elif opcode == 3:
                self.ta = ta
                self.ip += increment
                self.state = "in"
                return
            # output    
            elif opcode == 4:
                self.out = a
                self.state = "out"
                # print("out:", a)
            # jump if true    
            elif opcode == 5:
                if not a == 0:
                    self.ip = b
                    continue
            # jump if false
            elif opcode == 6:
                if a == 0:
                    self.ip = b
                    continue
            # less than
            elif opcode == 7:
                if a < b:
                    self.tape[tc] = 1
                else:
                    self.tape[tc] = 0
            # equals
            elif opcode == 8:
                if a == b:
                    self.tape[tc] = 1
                else:
                    self.tape[tc] = 0
                
            # halt    
            elif opcode == 99:
                self.halt = True
                self.state = "halt"
                # print("halt")
                return

            self.ip += increment
            
import itertools

iteer = itertools.permutations(range(5, 10), 5)

top = 0

for comb in iteer:
    
    cpu1 = cpu()
    cpu1.run()
    cpu1.inpu(comb[0])

    cpu2 = cpu()
    cpu2.run()
    cpu2.inpu(comb[1])

    cpu3 = cpu()
    cpu3.run()
    cpu3.inpu(comb[2])

    cpu4 = cpu()
    cpu4.run()
    cpu4.inpu(comb[3])

    cpu5 = cpu()
    cpu5.run()
    cpu5.inpu(comb[4])

    cpus = [cpu1, cpu2, cpu3, cpu4, cpu5]

    i = 0
    cur = 0

    while cpu5.state != "halt":
        
        # print("sending input:", cur, cpus[i].state)
        cpus[i].inpu(cur)
        # print("getting output", cpus[i].state)
        cur = cpus[i].out
        i += 1
        i %= 5
    
    top = max(top, cur)

print(top)