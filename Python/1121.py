#casos = int(input())
#for i in range(casos):
#  lista = []
#  lista2 = []
#  media = 0
#  num = 0
#  m1 = 0
#  cont = 0
#  porcent = 0
#  lista = input().split()
#  for y in lista:
#    y = int(y)
#    lista2.append(y)
#  num = lista2[0]
#  if len(lista2)==(num + 1):
#    m1 = sum(lista2[1:])
#    media = m1/num
#    for x in lista2:
#      if x == num:
#        pass
#      if x > media:
#        cont += 1
#    porcent = (cont/num) * 100
#    print('{:.3f}%'.format(porcent))
#else:
#  pass
casos=int(input())
for i in range(casos):
    lista=list(map(int,input().split()))
    if lista[0] >= 1 and lista[0] <= 1000:
        media = sum(lista[1:])
        media /= lista[0]
        cont=0
        for x in lista[1:]:
            if x > media:
                cont+=1
        porcent=(cont*100)/lista[0]
        print('{:.3f}%'.format(porcent))