v0 = int(input())
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())
v6 = int(input())
v7 = int(input())
v8 = int(input())
v9= int(input())
num = 0
lista = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9]
for i in lista:
    if i <= 0:
        print('X[{}] = 1'.format(num))
        num = num + 1
    else:
        print ('X[{}] = {}'.format(num, i))
        num = num + 1