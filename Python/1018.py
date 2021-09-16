valor = int(input())
print(valor)
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
not1 = int(valor/1)
print(not100,'nota(s) de R$ 100,00')
print(not50,'nota(s) de R$ 50,00')
print(not20,'nota(s) de R$ 20,00')
print(not10,'nota(s) de R$ 10,00')
print(not5,'nota(s) de R$ 5,00')
print(not2,'nota(s) de R$ 2,00')
print(not1,'nota(s) de R$ 1,00')