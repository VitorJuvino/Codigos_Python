
# BEE 1066

contador_par = 0
contador_impar = 0
contador_positivo = 0
contador_negativo = 0
lista = []

for i in range(5):
    n = int(input())
    lista.append(int(n))


for valor in lista[0:5:]:
    if valor % 2 == 0:
        contador_par += 1

    if valor % 2 != 0:
        contador_impar +=1

    if valor > 0:
        contador_positivo += 1

    elif valor < 0:
        contador_negativo += 1

print(contador_par, 'valor(es) par(es)')
print(contador_impar, 'valor(es) impar(es)')
print(contador_positivo, 'valor(es) positivo(s)')
print(contador_negativo, 'valor(es) negativo(s)')

        

        

        
