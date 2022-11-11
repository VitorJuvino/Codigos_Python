import os
os.system('cls')

# Exemplo 3
def main():

    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero: '))
    z = int(input('Terceiro: numero: '))

    # Verificando o maior
    if x > y and x > z:
        print(f'{x} é o maior')
    elif y > x and y > z:
        print(f'{y} é o maior')
    elif z > x and z > y:
        print(f'{z} é o maior')
    
    # Verificando o menor
    if x < y and x < z:
        print(f'{x} é o menor')
    elif y < x and y < z:
        print(f'{y} é o menor')
    elif z < x and z < y:
        print(f'{z} é o menor')

    # Verificando a igualdade
    if x == y or x == z:
        print(f'{x} Foi repetido')
    elif y == x or y == z:
        print(f'{y} Foi repetido')
    elif z == x or z == y:
        print(f'{z} Foi repetido')
    

main()