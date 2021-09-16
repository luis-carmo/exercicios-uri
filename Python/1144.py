casos = int(input())
cont1 = 1
cont2 = 0
for i in range(casos):
    print("{} {} {}".format(cont1, cont1**2, cont1**3))
    print("{} {} {}".format(cont1, ((cont1**2)+1), ((cont1**3)+1)))
    cont1 += 1