
#BEE1060

lista = []

for i in range(6):
    n = float(input())
    lista.append(float(n))

contador = 0

for x in range(6):

    if lista[x] > 0:
        contador += 1
print(contador, 'valores positivos')