valor = float(input())
not100 = int(valor/100)
valor = valor%100
not50 = int(valor/50)
valor = valor%50
not20 = int(valor/20)
valor = valor%20
not10 = int(valor/10)
valor = valor%10
not5 = int(valor/5)
valor = valor%5
not2 = int(valor/2)
valor = valor%2
moeda1 = int(valor/1)
valor = valor%1
moeda050 = int(valor/0.5)
valor = valor%0.5
moeda025 = int(valor/0.25)
valor = valor%0.25
moeda010 = int(valor/0.10)
valor = valor%0.10
moeda005 = int(valor/0.05)
valor = valor%0.05
moeda001 = int(valor/0.01)
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(not100))
print('{} nota(s) de R$ 50.00'.format(not50))
print('{} nota(s) de R$ 20.00'.format(not20))
print('{} nota(s) de R$ 10.00'.format(not10))
print('{} nota(s) de R$ 5.00'.format(not5))
print('{} nota(s) de R$ 2.00'.format(not2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(moeda1))
print('{} moeda(s) de R$ 0.50'.format(moeda050))
print('{} moeda(s) de R$ 0.25'.format(moeda025))
print('{} moeda(s) de R$ 0.10'.format(moeda010))
print('{} moeda(s) de R$ 0.05'.format(moeda005))
print('{} moeda(s) de R$ 0.01'.format(moeda001))