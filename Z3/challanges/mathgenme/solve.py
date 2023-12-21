from z3 import *

licen="c0d89f68c6e9c31f4da2e414eab48500e94c101a6e8a337292ab2bad7396a2c479557cedbe0f0df99539996971f0e056"
licen=[int(licen[i:i+2],16) for i in range(0,len(licen),2)]
s=Solver()
password=[BitVec(f"pwd_{i:02}", 8) for i in range(0, 48)]
licenseZ=[BitVec(f"licen_{i:02}", 8) for i in range(0, 48)]


c=0
for i in range(0,12):
    s.add((password[c]*ord('B')+password[c+1]*ord('g')+password[c+2]*ord('Y')+password[c+3]*ord('!'))==licenseZ[c])
    s.add((password[c+3]*ord('3')+password[c+2]*(-0x67)+password[c+1]*(-0x7d)+password[c]*ord('I'))==licenseZ[c+1])
    s.add(((password[c+2]*8)+password[c]*ord('6')+password[c+3]+password[c+1]*ord('q'))==licenseZ[c+2])
    s.add((password[c+1]*3+password[c]*ord('w')+password[c+3]*23+password[c+2]*25)==licenseZ[c+3])
    c+=4

for i in range(0,48):
    s.add(licenseZ[i]==licen[i])
    s.add(password[i]>=32)
    s.add(password[i]<=126)

 

if s.check() == sat:
    m = s.model()

    filtered_solution = sorted([(str(i), m[i]) for i in m if str(i)[0] == "p"])
    flag = ''.join(map(lambda x: chr(int(str(x[1]))), filtered_solution))
    print(flag)
else:
    print("No solution")