T =int(input())
for i in range(T):
    N=int(input())
    f=[0,1]
    if N>1:
        for j in range(2,N+1):
           
            f.append(f[j-2]+f[j-1])
        print('Fib({}) = {}'.format(N,f[N]))
    if N<=1:
        print('Fib({}) = {}'.format(N,f[N]))