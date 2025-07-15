import math
import sys
if len(sys.argv) < 2:
    print("Использование: python task2.py task2component1.txt task2component2.txt")
    sys.exit(1)

f = open(sys.argv[1]).readlines()
fv = open(sys.argv[2]).readlines()


xO = float(f[0][0])
yO = float(f[0][2])
r = float(f[1])
for i in fv:
    xT = float(i[0])
    yT = float(i[2])

    d = math.sqrt((xT - xO)**2 + (yT - yO)**2)

    if d > r:
        print(2)
    elif d == r:
        print(0)
    else: 
        print(1)

