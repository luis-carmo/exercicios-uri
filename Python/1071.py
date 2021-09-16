#x = int(input())
#y = int(input())
#a = y
#soma = 0
#while a <= x:
#    if a % 2 !=0:
#        soma = soma + a
#    a = a + 1
#print (y)

#x = int(input())
#y = int(input())
#
#maior = x if x > y else y
#menor = y if y < x else x
#menor+=1
#soma = 0
#
#while (menor < maior):
#    if(menor % 2 != 0):
#        soma+=menor
#    menor+=1
#print(soma)

x = int(input())
y = int(input())
maior = x if x > y else y
menor = y if y < x else x
res = 0
menor = menor + 1
while menor < maior:
    if menor % 2 !=0:
        res = res + menor
    menor = menor + 1
print(res)
