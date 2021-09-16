sal = float(input())
if sal > 0:
    if sal <= 2000:
        print ('Isento')
    if sal > 2000 and sal <= 3000:
        sal = sal - 2000
        imp = sal * (8/100)
        print ('R$ {:.2f}'.format(imp))
    if sal > 3000 and sal <= 4500:
        sal = sal - 3000
        imp1 = 1000 * (8/100)
        imp2 = sal * (18/100)
        imp = imp1 + imp2
        print ('R$ {:.2f}'.format(imp))
    if sal > 4500:
        sal = sal - 4500
        imp1 = 1000 * (8/100)
        imp2 = 1500 * (18/100)
        imp3 =sal * (28/100)
        imp = imp1 + imp2 + imp3
        print ('R$ {:.2f}'.format(imp))