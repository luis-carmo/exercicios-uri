valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
if a >= b and a >=c:
    m1 = a
    if b >= c:
       m2 = b
       m3 = c
    else:
        m2 = c
        m3 = b
if b >= a and b >= c:
    m1 = b
    if a >= c:
        m2 = a
        m3 = c
    else:
        m2 = c
        m3 = a
if c >= a and c >= b:
    m1 = c
    if b >= a:
        m2 = b
        m3 = a
    else:
        m2 = a
        m3 = b
a = m1
b = m2
c = m3
if a >= (b+ c):
    print('NAO FORMA TRIANGULO')
else:
    if (a**2) == (b**2 + c**2):
        print('TRIANGULO RETANGULO')
    if (a**2) > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    if (a**2) < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if (a == b == c):
        print ('TRIANGULO EQUILATERO')
    if (a==b !=c) or (a==c !=b) or (b==c !=a):
        print('TRIANGULO ISOSCELES')