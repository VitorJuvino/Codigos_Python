import os
os.system('cls')

# Questao 2
# Ele recebe o numero de telefone, caso seja digitado com espaço ele faz a juncao,
# e depois informa de forma separada o DDD e o numero.


numero = str(input('Informe o seu número de telefone com o DDD: '))

numero = numero.replace(' ', '')
print('')
print(f'O seu DDD é ({numero[0:2]}) que legal!')
print('')
print(f'E o seu número: {numero[2:12]}')
print('')
