T = int(input())
x = 0
for N in range(1000):
    print ('N[{}] = {}'.format(N, x))
    x = x + 1
    if x == (T):
        x = 0