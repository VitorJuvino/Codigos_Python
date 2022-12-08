
# Questao 1
# Ele recebe seu nome formata para que as primeiras letras fiquem maisculas,
# Separando o seu nome e elogiando o segundo nome.

import os
import time
os.system('cls')


nome = str(input('Digite o seu nome completo: '))

nome = nome.title()
s = nome.split()

print('Olá {}' .format(s[0]))
time.sleep(1)
print('Gostei muito do seu sobrenome {}' .format(s[1]))
print('')

