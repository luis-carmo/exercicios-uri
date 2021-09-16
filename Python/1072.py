dentro = 0
fora = 0
N = int(input())
for i in range (N):
    X = int(input())
    if X in range(10,20):
        dentro = dentro + 1
    else:
        fora = fora + 1
print ('{} in'.format(dentro))
print('{} out'.format(fora))