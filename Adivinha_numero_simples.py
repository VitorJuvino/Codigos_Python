from random import randint

cont1 = 0
cont2 = 4
while True:

    random = randint(1, 10)
    cont1 = cont1 + 1
    cont2 = cont2 - 1
    n = int(input(f'Digite um numero entre 1 e 10 (Voce tem {cont2} chances): '))

    if n == random:
        print("=============")
        print("Você acertou!")
        print("=============")
        break
    
    elif cont1 == 3:
        break


   
print(f'Total de tentativas: {cont1}')

print(f'Numero secreto é: {random}')

