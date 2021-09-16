i, f = input().split()
i = int(i)
f = int(f)
t = 0
if  f > i:
    t = f - i
    print('O JOGO DUROU {} HORA(S)'.format(t))
else:
    t = (24 - i) + f
    print('O JOGO DUROU {} HORA(S)'.format(t))