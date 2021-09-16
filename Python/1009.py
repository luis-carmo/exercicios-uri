nome = str(input())
salario = float(input())
vendas = float(input())
comissao = 0.15*vendas
bonus = salario + comissao
print ('TOTAL = R$ {:0.2f}'.format(bonus))