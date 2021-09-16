seg_minuto = 60
seg_hora = 3600
tempo = int(input())
tempohor = int(tempo/seg_hora)
tempo = tempo%seg_hora
tempomin = int(tempo/seg_minuto)
tempo = tempo%seg_minuto
temposec = tempo
print('{}:{}:{}'.format(tempohor,tempomin,temposec))