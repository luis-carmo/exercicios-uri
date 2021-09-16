sal = float(input())
if sal > 0:
    if sal <= 400:
        re = sal * (15/100)
        nsal = re + sal
        p = 15
    elif sal > 400 and sal <= 800:
        re = sal* (12/100)
        nsal = re + sal
        p = 12
    elif sal > 800 and sal <= 1200:
        re = sal* (10/100)
        nsal = re + sal
        p = 10
    elif sal > 1200 and sal <= 2000:
        re = sal* (7/100)
        nsal = re + sal
        p = 7
    elif sal >2000:
        re = sal* (4/100)
        nsal = re + sal
        p = 4
print('Novo salario: {:.2f}'.format(nsal))
print('Reajuste ganho: {:.2f}'.format(re))
print('Em percentual: {} %'.format(p))