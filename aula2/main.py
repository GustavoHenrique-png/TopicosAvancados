a = 2
b = -5
c = 4

x1 = 4
x2 = 1

if x1 == x2:
    print('As raizes não pode ser iguais')
elif x1 < 0 and x2 < 0:
    print('Ambas raizes nao podem ser menores que zero')
else:
    y1 = (a*x1**2) + (b*x1) + c
    y2 = (a*x2**2) + (b*x2) + c

    fa = abs(y1) + abs(y2)
    print(fa)