I = 0
J = 7
cont = 1
cont2 = 3
while I <=14:
    print('I={} J={}'.format(cont, J))
    J = J - 1
    I = I + 1
    cont2 = cont2 - 1
    if cont2 == 0:
        cont = cont + 2
        cont2 = 3
        J = 7