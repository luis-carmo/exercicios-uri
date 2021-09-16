n = 0
soma = 0
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
lista = [a, b, c, d, e, f]
for numero in lista:
    if numero > 0:
        n = n + 1
        soma = soma + numero
print(n,'valores positivos')
media = soma/n
print('{:0.1f}'.format(media))