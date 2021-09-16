num = 0
par = []
impar = []
x = 0
y = 0
while num<15:
    a = int(input())
    if a % 2 == 0:
        par.append(a)
        x = x + 1
        if x == 5:
            for cont in range (0,5):
                print('par[{}] = {}'.format(cont, par[cont]))
            par = []       
            x = 0
    else:
        impar.append(a)
        y = y + 1
        if y == 5:
            for cont in range(0,5):
                print('impar[{}] = {}'.format(cont, impar[cont]))
            impar = []
            y = 0
    num = num + 1
if y > 0:
    for cont in range(y):
        print('impar[{}] = {}'.format(cont, impar[cont]))
if x > 0:
    for cont in range(x):
        print('par[{}] = {}'.format(cont, par[cont]))