cod,qtd = input().split()
cod, qtd = int(cod), int(qtd)
if cod == 1:
    prec = qtd * 4.00
    print('Total: R$ {:.2f}'.format(prec))
if cod == 2:
    prec = qtd * 4.50
    print('Total: R$ {:.2f}'.format(prec))
if cod == 3:
    prec = qtd * 5.00
    print('Total: R$ {:.2f}'.format(prec))
if cod == 4:
    prec = qtd * 2.00
    print('Total: R$ {:.2f}'.format(prec))
if cod == 5:
    prec = qtd * 1.50
    print('Total: R$ {:.2f}'.format(prec))