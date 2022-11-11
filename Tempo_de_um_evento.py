
# bee1061

import os

os.system('cls')

def tempo_evento():
    # Fazendo o recebimento dos dados
    dia_i = input().split()
    hora_i = input().split()
    dia_f = input().split()
    hora_f = input().split()
    # Separando os dados
    di, df = int(dia_i[1]), int(dia_f[1]) # Separando somente o dia
    hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4]) # Separando a hora, minuto e segundos da variavel hora_i
    hf, mf, sf = int(hora_f[0]), int(hora_f[2]), int(hora_f[4]) # Separando a hora, minuto e segundos da variavel hora_f


    minuto_seg = 60
    hora_seg = minuto_seg * 60
    dia_seg = hora_seg * 24
    i = si + mi*minuto_seg + hi*hora_seg + di*dia_seg
    f = sf + mf*minuto_seg + hf*hora_seg + df*dia_seg

    if i < f:
        tempo = f - i
        dias = int(tempo/dia_seg)
        tempo = tempo%dia_seg
        horas = int(tempo/hora_seg)
        tempo = tempo%hora_seg
        minutos = int(tempo/minuto_seg)
        tempo = tempo%minuto_seg
        segundos = tempo
        print(f'{dias} dias (s)')
        print(f'{horas} horas (s)')
        print(f'{minutos} minutos (s)')
        print(f'{segundos} segundos (s)')

tempo_evento()
    
