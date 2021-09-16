cases = int(input())
som = 0
maior = 0
menor = 0
for i in range(cases):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X > Y:
        maior = X
        menor = Y
        menor = menor + 1
    elif Y > X:
        maior = Y
        menor = X
        menor = menor + 1
    while menor < maior:
        if menor % 2 != 0:
            som = som + menor
        menor = menor + 1
    print(som)
    som = 0