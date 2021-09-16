n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1),float(n2),float(n3),float(n4)
m1 = ((n1*2) + (n2*3) + (n3*4) + n4)/10
print('Media: {:.1f}'.format(m1))
if m1 >= 7:
    print('Aluno aprovado')
elif m1 < 5:
    print('Aluno reprovado')
else:
    print('Aluno em exame')
    n5 = float(input())
    print('Nota do exame: {:.1f}'.format(n5))
    m2 = (m1 + n5)/2
    if m2 >= 5:
        print('Aluno aprovado')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado')
        print('Media final: {:.1f}.'.format(m2))