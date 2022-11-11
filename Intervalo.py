
# Atividade Intervalo do beecrowd



numb = float(input())

if 0 <= numb <= 25:
    print(f'Intervalo [0,25]')

if 25 < numb <= 50:
    print(f'Intervalo (25,50]')

if 50 < numb <= 75:
    print(f'Intervalo (50,75]')

if 75 < numb <= 100:
    print(f'Intervalo (75,100]')

if numb < 0 or numb > 100:
    print(f'Fora de intervalo')


