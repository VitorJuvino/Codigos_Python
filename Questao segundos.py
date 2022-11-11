# Segundos
# 22-02-22, Vitor

# Ler da entrada um tempo em segundos
tempo = int(input('Digite a quantidade de segundos '))
# Fazer a decomposiçao dos segundos
# Horas
hora = tempo // 3600
# resto = tempo % {tempo} obs: outra opçao
# Minutos
minutos = tempo % 3600 // 60
# resto1 = resto % 60
# Segundos 
segundo = tempo % 3600 % 60
# Exibir o resultado para o usuário.
print(f'{hora}:{minutos}:{segundo}')
