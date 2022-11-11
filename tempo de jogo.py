# Bee1046
# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, 
# sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima 
# de 1 hora e máxima de 24 horas.


import os

os.system('cls')

a, b = map(int,input().split())

def horas_do_jogo():

    if a < b:
        t = b - a

    else:
        t = (24 - a) + b
    print(f'O JOGO DUROU {t} HORA(S)')

horas_do_jogo()
