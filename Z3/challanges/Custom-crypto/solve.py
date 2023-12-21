from z3 import *

enc=[28, 24, 1, 9, 9, 19, 93, 93, 94, 2, 26, 13, 6, 92, 61, 11, 15, 39, 91, 91, 20, 28, 54, 8, 17, 89, 23, 61]
key=[]
s=Solver()

dec = [BitVec(f"dec_{i:02}", 8) for i in range(0, len(enc))]
key = [BitVec(f"key_{i:02}", 8) for i in range(0, 4)]


for i, v in enumerate('pwned'):
    s.add(dec[i] == ord(v))

for i in range(0, len(enc)):
    chunk = i // 4
    offset = i % 4
    s.add((dec[i] + chunk) ^ key[offset] == enc[i])
    s.add(And(dec[i]>=32, dec[i]<=126))

s.check()
m=s.model()

filtered_solution = sorted([(str(d), m[d]) for d in m if str(d)[0]=="d"])
flag = ''.join(map(lambda x: chr(int(str(x[1]))), filtered_solution))

print(flag)