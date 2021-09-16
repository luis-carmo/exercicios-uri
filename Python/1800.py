Q, E = input().split()
Q = int(Q)
E = int(E)
escl = input().split()
sem = []
if (len(escl)) == E:
    for i in range (E):
        escl[i] = int(escl[i])
    for i in range(Q):
        esc = int(input())
        if esc in escl or esc in sem:
            print('0')
        else:
            print('1')
            sem.append(esc)