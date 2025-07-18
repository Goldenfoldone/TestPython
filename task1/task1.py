import sys

if len(sys.argv) < 2:
    print("Использование: python task1.py 3 4")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

l = 1
osnovmassiv = [0]
summa = ''

while osnovmassiv[-1] != 1:
    for i in range(m):
        osnovmassiv.append(l)
        if l == n:
            l = 1
        else:
            l += 1
    l = osnovmassiv[-1]
for i in range(1,len(osnovmassiv) - 1, m):
    summa += str(osnovmassiv[i])
print(summa)