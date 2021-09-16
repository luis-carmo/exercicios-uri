dia_1 = input().split()
dia1 = int(dia_1[1])
tempo_1 = input().split()
h1, m1, seg1 = int(tempo_1[0]), int(tempo_1[2]), int(tempo_1[4])
dia_2 = input().split()
dia2 = int(dia_2[1])
tempo_2 = input().split()
h2, m2, seg2 = int(tempo_2[0]), int(tempo_2[2]), int(tempo_2[4])

minseg = 60
horaseg = minseg*60
diaseg = horaseg*24
dia_i = dia1*diaseg +h1*horaseg + m1*minseg + seg1
dia_f = dia2*diaseg +h2*horaseg + m2*minseg + seg2
if dia_i < dia_f:
    tempo = dia_f - dia_i
    dia = int(tempo/diaseg)
    tempo = tempo%diaseg
    hora = int(tempo/horaseg)
    tempo = tempo%horaseg
    minuto = int(tempo/minseg)
    tempo = tempo%minseg
    seg = tempo
    print (dia,'dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(hora, minuto, seg))