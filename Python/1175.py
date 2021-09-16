lista=[]
for i in range(20):
    valores=int(input())
    lista.append(valores)
vetor=lista[::-1]
for i in range(20):
    print('N[{}] = {}'.format(i,vetor[i]))