from z3 import *

o = Optimize()
x = Real('x')
y = Int('y')

ans = solve(x ** 4 - x ** 2 + 2 * x + 1 == 0)

s = Solver()

p, q, r = Bools("p q r")
# s.add(Or(Not(p), Not(q), r) == Or(Not(Or(p, q)), r))
s.add(Or(And(p, Or(p, q)), Not(p)))
print(s.check())
print(s.model())
