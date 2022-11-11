
# Beecrowd 1047

import os

os.system('cls')

h1, m1, h2, m2, = map(int,input().split())

def tempo_do_jogo():

    if h1 < h2:
        horas = h2 - h1
        
        if m1 < m2:
            minutos = m2 - m1
        
        if m1 > m2:
            horas = horas - 1
            minutos = (60 - m1) + m2

        if m1 == m2:
            minutos = 0

    if h1 > h2:
        horas = (24 - h1) + h2

        if m1 < m2:
            minutos = m2 - m1

        if m1 > m2:
            horas = horas - 1
            minutos = (60 - m1) + m2
    
        if m1 == m2:
            minutos = 0
            
    if h1 == h2:
    
        if m1 < m2:
            minutos = m2 - m1
            horas = 0
    
        if m1 > m2:
            minutos = (60 - m1) + m2
            horas = 23
    
        if m1 == m2:
            horas = 24
            minutos = 0

    
        
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

tempo_do_jogo()








