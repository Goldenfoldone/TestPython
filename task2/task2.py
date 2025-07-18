import math
import sys
if len(sys.argv) < 2:
    print("Использование: python task2.py task2component1.txt task2component2.txt")
    sys.exit(1)

f = open(sys.argv[1]).readlines()
fv = open(sys.argv[2]).readlines()


xO = float(f[0].split(' ')[0])
yO = float(f[0].split(' ')[1])
r = float(f[1])
for i in fv:
    xT = float(i.split(' ')[0])
    yT = float(i.split(' ')[1])

    d = math.sqrt((xT - xO)**2 + (yT - yO)**2)

    if d > r:
        print(2)
    elif d == r:
        print(0)
    else: 
        print(1)

