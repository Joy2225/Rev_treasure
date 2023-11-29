from z3 import *
s = Solver() 
x = Bool("x")
s.add(And(x,Not(x)))
s.check()
print(s.model())