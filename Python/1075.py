N = int(input())
a = 1
while a < 10000:
    if a % N == 2:
        print(a)
    a = a + 1