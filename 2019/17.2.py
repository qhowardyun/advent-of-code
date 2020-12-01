def find_subroutines(instructions):
    # we know that the first substring must start from the first instruction
    # and that the last substring must end with the last instruction
    # so we can brute force all possible A and C and see if the remaining fragments are covered by the shortest fragment
    n = len(instructions)
    # brute force all possible A and C (100 possibilities total)
    for a in range(1, 10):
        A = instructions[0:a]
        for c in range(1, 10):
            C = instructions[-c:]
            covered = [False for i in instructions]
            # update coverage due to A
            for i in range(n - len(A)):
                if instructions[i : (i + len(A))] == A:
                    for j in range(i, i + len(A)):
                        covered[j] = True
            # update coverage due to B
            for i in range(n - len(C)):
                if instructions[i : (i + len(C))] == C:
                    for j in range(i, i + len(C)):
                        covered[j] = True
            # get fragments not covered by A or C, and keep track of shortest fragment
            fragments = []
            fragment = []
            shortest = [0] * n
            for i in range(n):
                if covered[i] == True:
                    if len(fragment) > 0:
                        fragments.append(fragment.copy())
                        if len(fragment) < len(shortest):
                            shortest = fragment.copy()
                    else:
                        continue
                if covered[i] == False:
                    fragment.append(instructions[i])
            # check if the shortest fragment covers longer fragments
            valid = True
            for fragment in fragments:
                if shortest == fragment:
                    continue
                elif len(shortest) < len(fragment):
                    reps = len(fragment) // len(shortest)
                    if shortest * reps == fragment:
                        continue
                valid = False
                break
            # print out comprresion
            if valid:
                B = shortest
                print(f"{A}\n{shortest}\n{B}")
                
                
find_subroutines("R,4,L,10,L,10,L,8,R,12,R,10,R,4,R,4,L,10,L,10,L,8,R,12,R,10,R,4,R,4,L,10,L,10,L,8,L,8,R,10,R,4,L,8,R,12,R,10,R,4,L,8,L,8,R,10,R,4,R,4,L,10,L,10,L,8,L,8,R,10,R") 