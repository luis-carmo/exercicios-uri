pos = 0
for i in range (100):
    vetor = float(input())
    if vetor <= 10:
        print('A[{}] = {:0.1f}'.format(pos, vetor))
    pos = pos + 1