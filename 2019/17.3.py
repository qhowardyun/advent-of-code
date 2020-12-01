import cpu

cpu = cpu.CPU("17.in")

cpu.tape[0] = 2

inpu = "A,B,A,B,A,C,B,C,A,C\nR,4,L,10,L,10\nL,8,R,12,R,10,R,4\nL,8,L,8,R,10,R,4\nn\n"


for char in inpu:
    cpu.stdin.append(ord(char))
    print(ord(char))



cpu.run()

while len(cpu.stdout) > 0:
    
    print(cpu.stdout.pop())
