import sys
import math
if len(sys.argv) < 2:
    print("Использование: python task4.py task4components.txt")
    sys.exit(1)

summa = 0
f = open(sys.argv[1]).readlines()
ca = [int(item.strip()) for item in f]


for i in ca:
    summa += int(i)

averageValue = summa // len(ca)
summa = 0
for i in ca:
    summa = summa + math.fabs(int(i) - averageValue)
print(int(summa))