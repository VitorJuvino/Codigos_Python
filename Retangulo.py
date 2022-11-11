# Retangulo
# 22-02-22,  Vitor

# Solicitar a base do retangulo 
base = float(input('Qual a base do retângulo? '))
# Solicitar a altura do retangulo
altura = int(input('Qual a altura do retângulo? '))
# Calcular a área 
area = base * altura
# Calcular o perimetro
perimetro = 2 * (base + altura)
# Exibir a área e o perímetro do retângulo
print('A área do retângulo é de {:.2f} centímetros quadrados.\n' # \n serve para a quebra de linha
'O perímetro do retângulo é de {:.2f}'.format(area,perimetro) # foi feita a formataçao da s casas decimais
)