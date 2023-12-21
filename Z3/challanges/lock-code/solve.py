from z3 import *

a,b,c=Ints('a b c')
code=[a,b,c]
s=Solver()

def GoodValueBadPlace(nums, count):
    exps = []
    for i in range(len(nums)):
        for j in range(len(code)):
            if i == j:
                continue
            else:
                exps.append((code[j] == nums[i]))
    return Sum(exps) == count


#Also works and more optimized
# s.add(Or(code[0] == 2, code[1] == 9, code[2] == 1))
# # one number is correct but wrong placed
# s.add(GoodValueBadPlace([2, 4, 5], 1))
# # two numbers are correct but wrong placed
# s.add(GoodValueBadPlace([4, 6, 3], 2))
# # nothing is correct
# s.add(And(code[0] != 5, code[1] != 7, code[2] != 9))
# # one number is correct but wrong placed
# s.add(GoodValueBadPlace([5, 6, 9], 1))

s.add(Or(a==2, b==9, c==1))
#one number is correct but wrong placed
s.add(Sum(a==4,a==5,b==2,b==5,c==2,c==4)==1)
#two numbers are correct but wrong placed
s.add(Sum(a==6,a==3, b==4,b==3, c==4,c==6)==2)
s.add(And(a!=5, b!=7, c!=8))
#one number is correct but wrong placed
s.add(Sum(a==6,a==9, b==5,b==9,c==5,c==6)==1)
s.check()
print(s.model())