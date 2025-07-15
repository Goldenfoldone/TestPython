n = int(input())
m = int(input())

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