contador = 0

acumulador = 0

aluno = input("Digite o nome do aluno: ")

while(True):

   try:

       contador += 1

       notas = input(f"Digite a nota {contador} do aluno {aluno}: ")

       acumulador += int(notas)

       print(f"A média do aluno {aluno} é {acumulador/contador:.2f} \n")

   except: break

# Explicação:

# 1) Começamos definindo o contador e acumulador como 0:

# contador = 0

# acumulador = 0

# 2) Em seguida solicitamos ao usuário o nome do aluno:

# aluno = input("Digite o nome do aluno: ")

# 3) Criamos um loop com while que nunca se encerra e utilizamos o comando try para tentar executar o código que está por vir e no caso de existir um except, iremos usar a interrupção break confrome pedido no enunciado:

# while(True):

#    try:

#        {código que será executado...}

#    except: break

# 4) No escopo do try começamos incrementando valor ao nosso contador, era 0 e passa a se tornar 1. Em seguida solicitamos ao usuário a nota 1 do aluno que, ao ser digitado e confirmado, é somado ao acumulador. Para finalizar, imprimimos o resultado final para o usuário:

# while(True):

#    try:

#        contador += 1

#        notas = input(f"Digite a nota {contador} do aluno {aluno}: ")

#        acumulador += int(notas)

#        print(f"A média do aluno {aluno} é {acumulador/contador:.2f} \n")

#    except: break

# OBSERVAÇÃO:

# O código somente é interrompido se ocorrer uma exceção e uma forma fácil de executar isso é informando um valor diferente do tipo inteiro para a variável notas, neste caso, informe um caracter ou mesmo aperte o enter sem incluir nenhum valor.

# Em caso de não interrupção, o código do escopo try será executado infinitamente e nunca terá fim.