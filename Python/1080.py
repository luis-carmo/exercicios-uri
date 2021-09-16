maior = 0
for i in range(100):
    a = int(input())
    if (a > maior):
        maior = a
        pos = i + 1
print(maior)
print(pos)