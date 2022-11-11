
# Questao par ou impar



def par_impar():

    # Recebendo os valores...
    nome1, opcao1, nome2, opcao2 = input().split()

    k, p = input().split()
    
    # Atribuindo se sao strings ou inteiros
    nome1 = str(nome1)
    nome2 = str(nome2)
    opcao1 = str(opcao1)
    opcao2 = str(opcao2)
    k = int(k)
    p = int(p)

    # Convertendo para maisculo a opcao de par e impar
    opcao1 = opcao1.upper()
    opcao2 = opcao2.upper()


    # Caso sejam dois pares ou dois impares nao haverar vencedor
    if opcao1 == opcao2:
        print('Nao pode haver dois pares ou dois impares')

    # Caso o valor dos numeros seja PAR, vai imprimir o nome do jogador que escolheu PAR.
    elif (k + p) %2 == 0:
        if opcao1 == 'PAR':
            print(nome1)

        elif opcao2 == 'PAR':
            print(nome2)

    # Caso contrario vai imprimir o nome do jogador que escolheu IMPAR.
    elif (k + p) %2 != 0:
        if opcao1 == 'IMPAR':
            print(nome1)
        elif opcao2 == 'IMPAR':
            print(nome2)


    else:
        print()

        




par_impar()
