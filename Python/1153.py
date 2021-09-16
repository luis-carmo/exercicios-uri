while True:
    try:
        M, N = input().split()
        M = int(M)
        N = int(N)
        fat1 = 1
        fat2 = 1
        resultado1 = 1
        resultado2 = 1
        while fat1 <= M:
            resultado1 *= fat1
            fat1 += 1
        resultado = 1
        while fat2 <= N:
            resultado2 *= fat2
            fat2 += 1
        res = resultado1 + resultado2
        print(res)
    except:
        break