# <u>Boolean</u>
```python
#Taken from hacktricks website
#pip3 install z3-solver
from z3 import *
s = Solver() #The solver will be given the conditions

x = Bool("x") #Declare the symbos x, y and z
y = Bool("y")
z = Bool("z")

# (x or y or !z) and y
s.add(And(Or(x,y,Not(z)),y))
s.check() #If response is "sat" then the model is satifable, if "unsat" something is wrong
print(s.model()) #Print valid values to satisfy the model
```

Majorly all the things are explained in the comments. One thing whose exact explanation I was looking for is the **`add`** function. 
- s.add(constraints) - Basically it gives the solver the constraints
Now the above code is can be satisfied by some specific values of x, y and z.
The output is:-
```
[z = False, y = True, x = False]
```

Now if you try to give something which cannot be solved. For example, if we give something as (x AND !x) which can never be true, then it throws an exception
```python
from z3 import *
s = Solver() 
x = Bool("x")
s.add(And(x,Not(x)))
s.check()
print(s.model())
```

**Output:**
```
Traceback (most recent call last):
  File "/home/joy/.local/lib/python3.10/site-packages/z3/z3.py", line 7131, in model
    return ModelRef(Z3_solver_get_model(self.ctx.ref(), self.solver), self.ctx)
  File "/home/joy/.local/lib/python3.10/site-packages/z3/z3core.py", line 4185, in Z3_solver_get_model
    _elems.Check(a0)
  File "/home/joy/.local/lib/python3.10/site-packages/z3/z3core.py", line 1505, in Check
    raise self.Exception(self.get_error_message(ctx, err))
z3.z3types.Z3Exception: b'there is no current model'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/joy/bi0s/Learning/Z3/test.py", line 6, in <module>
    print(s.model())
  File "/home/joy/.local/lib/python3.10/site-packages/z3/z3.py", line 7133, in model
    raise Z3Exception("model is not available")
z3.z3types.Z3Exception: model is not available
```

# <u>Integers/Simplify/Reals</u>

```python
#Taken from hacktricks website
from z3 import *

x = Int('x')
y = Int('y')
#Simplify a "complex" ecuation
print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))
#And(x >= 2, 2*x**2 + y**2 >= 3)

#Note that Z3 is capable to treat irrational numbers (An irrational algebraic number is a root of a polynomial with integer coefficients. Internally, Z3 represents all these numbers precisely.)
#so you can get the decimals you need from the solution
r1 = Real('r1')
r2 = Real('r2')
#Solve the ecuation
print(solve(r1**2 + r2**2 == 3, r1**3 == 2))
#Solve the ecuation with 30 decimals
set_option(precision=30)
print(solve(r1**2 + r2**2 == 3, r1**3 == 2))
```

**Output:**
```
And(x >= 2, 2*x**2 + y**2 >= 3)
[r1 = 1.2599210498?, r2 = -1.1885280594?]
None
[r1 = 1.259921049894873164767210607278?,
 r2 = -1.188528059421316533710369365015?]
None
```

The above code is pretty straightforward with the comments and the output. One doubt which might occur is why **`None`** is being printed. It is due to the fact that Z3's **`solve`** method, when used with the Real numbers and an irrational equation, may not always provide a precise solution. The floating-point arithmetic involved in solving equations with irrational numbers can sometimes lead to numerical imprecision, and Z3 might not be able to find an exact solution.

# <u> Printing model </u>

```python
from z3 import *

x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
s.check()

m = s.model()
print ("x = %s" % m[x])
for d in m.decls():
    print("%s = %s" % (d.name(), m[d]))
```

**Output:**
```
x = 3/2
y = 2
x = 3/2
z = 0
```

**Print Variable Values:**    
`print("x = %s" % m[x])`
This line prints the value assigned to the variable `x` in the satisfying model.

**Print All Variable Values:**
```
for d in m.decls():
	print("%s = %s" % (d.name(), m[d]))
```
This loop iterates over all declarations in the model (`m.decls()`), printing the name and value of each variable in the satisfying assignment.

In summary, this code sets up a system of real variables and constraints using the Z3 library, checks if there exists an assignment of values to the variables that satisfies the constraints, and then prints the values of the variables in a satisfying assignment if one is found.

