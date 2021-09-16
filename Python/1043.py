valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
if (A < B + C) and (B < A + C) and (C < A + B): 
    perim = A + B + C
    print('Perimetro = {:0.1f}'.format(perim))
else:
    area = ((A+B)*C)/2
    print('Area = {:0.1f}'.format(area))