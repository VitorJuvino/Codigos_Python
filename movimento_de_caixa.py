

entradas = []
saidas = []
cx_inicial = 0

def principal():

    
    while True:

        print("===Movimento do Caixa===")
        print("Dia **/**/**")
        print("1 - Adicionar Entrada")
        print("2 - Adicionar Saida")
        print("3 - Ve Movimento do dia")
        cx_inicial = int(input("Digite o valor Caixa Inicial: "))
        opcao = int(input("Digite o opção desejada: "))   

        if opcao == 1:

            e = float(input("Digite o valor: "))
            entradas.append(e)
        
        elif opcao == 2:

            s = float(input("Digite o valor: "))
            saidas.append(s)

        elif opcao == 3:

            total_entradas = sum(entradas)
            total_saidas = sum(saidas)

            print("Entradas ",entradas)
            print("Saidas ",saidas)
            print("TOTAL: ", )






principal()