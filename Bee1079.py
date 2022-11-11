

quant = int(input())

for c in range(1 , quant + 1 ):
    notas = input().split()
    nota1,nota2,nota3 = notas
    print('{:.1f}'.format((float(nota1) * 2 + float(nota2) * 3 + float(nota3) * 5) / 10))