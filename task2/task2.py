import math
import sys
if len(sys.argv) < 2:
    print("Использование: python task2.py task2component1.txt task2component2.txt")
    sys.exit(1)

f = open(sys.argv[1]).readlines()
fv = open(sys.argv[2]).readlines()


xO = int(f[0][0])
yO = int(f[0][2])
r = int(f[1])
print(fv)
for i in fv:
    xT = int(i[0])
    yT = int(i[2])

    d = math.sqrt((xT - xO)**2 + (yT - yO)**2)

    if d > r:
        print(2)
    elif d == r:
        print(0)
    else: 
        print(1)

