idade = int(input())
ano = 365
mes = 30
tempoano = int(idade/ano)
idade = idade%ano
tempomes = int(idade/mes)
idade = idade%mes
tempodias = idade
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(tempoano,tempomes,tempodias))