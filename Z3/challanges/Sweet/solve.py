from z3 import *

for input in range(1,32):
    
    s=Solver()
    flag=[BitVec(f"flag_{i}", 8) for i in range(input)]
    sum=BitVecVal(0,64)

    

    for i in range(input):
        # s.add(And(flag[i]>=32, flag[i]<=126))
        sum+=ZeroExt(64-8,flag[i])
        sum<<=1

    s.add(sum==0x2D64A)

    if s.check() == sat:
        m=s.model()
        print(m)
        filtered_soln=sorted([(str(d), m[d]) for d in m])
        print(filtered_soln)
        f = "".join([f"{int(str(x[1]), 10):x}" for x in filtered_soln])
        print(f)
        break

        # solution = sorted([(d, m[d]) for d in m], key=lambda x: str(x[0]))
        # flag = "".join([f"{int(str(x[1]), 10):x}" for x in solution])

        # # print(solution)
        # print(flag)
        # break

    else:
        print("Not there"+str(input))
