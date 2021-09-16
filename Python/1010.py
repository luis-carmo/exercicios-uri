linha1 = input().split()
cod1 = int(linha1[0])
n1 = int(linha1[1])
v1 = float(linha1[2])
valor1 = n1 * v1
linha2 = input().split()
cod2 = int(linha2[0])
n2 = int(linha2[1])
v2 = float(linha2[2])
valor2 = n2 * v2
vt = valor1 + valor2
print ('VALOR A PAGAR: R$ {:0.2f}'.format(vt))