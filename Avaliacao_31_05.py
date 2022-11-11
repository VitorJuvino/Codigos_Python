
# Questao 2


lista = []


while True:
    n = int(input('Digite os numeros: ')) # pedindo a entrada
    if n == 0:                            # inserindo o 0 para parar
       break
    lista.append(n)                       # adicionando os valores na lista 

    lista = lista

print(lista[::-1])                       # Imprimindo a lista com os valores inversos


# Questao 3

alunos = int(input('Informe a quantidade de alunos: '))
erros = 0
posicao = 0


for i in range(alunos):

    teste = input('Informe o resultado do teste aplicado: ')
    quant_erros = teste.count('f')

    if erros <= quant_erros:
        erros = quant_erros
        posicao = i + 1

print(f'O aluno {posicao} errou {erros} questoes')

        
    
# Questao 4


caracteres = ['a','a','e','f','f']
numb = [0,0,0,1,1,1,2,3,3,3,4,5]

def re_dupli(dados):

    re_dupli = []
    
    for n in dados:
        
        if n not in re_dupli:
            re_dupli.append(n)
    
    return re_dupli

print(re_dupli(caracteres))
print(re_dupli(numb))

re_dupli()


