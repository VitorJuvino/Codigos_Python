import os
os.system('cls')

# Questao 3
# Aqui fizemos uma simulacao de um cadastro

print('CADASTRO')
print('')

nome = str(input('Digite o seu nome completo: '))
ano = int(input('Digite o ano de seu nascimento (você de ser maior de 18 anos): '))



if ano <= 2004:

    s = nome.split()
    print('')
    print('O seu nome de usuário será {}@aluno.edu.br' .format(s[1]))
    print('')
    print('Obrigado por acessar o nosso site {}' .format(s[0]))
    print('')


else:
    print('Você é menor de menor de idade')


