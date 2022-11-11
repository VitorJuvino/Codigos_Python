
contador = 0

while True:
    
    lista = [7]
    contador = contador + 1
    n = int(input('Digite um numero entre 1 e 10 (Voce tem 3 chances): '))
    if contador == 3:
        break

    if n in lista:
        break   
   
print(f'Total de tentativas: {contador}')

print(f'Numero secreto é: {lista}')
