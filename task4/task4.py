import sys
import math
if len(sys.argv) < 2:
    print("Использование: python task4.py task4components.txt")
    sys.exit(1)

summa = 0
f = open(sys.argv[1]).readline().split(',')

for i in f:
    summa += int(i)

averageValue = summa // len(f)
summa = 0
for i in f:
    summa = summa + math.fabs(int(i) - averageValue)
print(int(summa))