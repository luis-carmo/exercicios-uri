N = int(input())
i = 1
if N > 5 and N < 2000:
    while i <= N:
        if i%2 == 0:
            res = i**2
            print('{}^2 = {}'.format(i, res))
        i = i + 1