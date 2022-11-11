# Questao Cédulas da segunda lista do beecrowd

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) 
# no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
# A seguir mostre o valor lido e a relação de notas necessárias

# Exemplo de Entrada: 576

# Exemplo de Saída;	
# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00


def main():

 valor = int(input())

 nota100 = valor // 100
 nota50 = valor % 100 // 50
 nota20 = valor % 100 % 50 // 20
 nota10 = valor % 100 % 50 % 20 // 10
 nota5 = valor % 100 % 50 % 20 % 10 // 5
 nota2 = valor % 100 % 50 % 20 % 10 % 5 // 2
 nota1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1

 print(f'{valor}')
 print(f'{nota100} nota(s) de R$ 100,00')
 print(f'{nota50} nota(s) de R$ 50,00')
 print(f'{nota20} nota(s) de R$ 20,00')
 print(f'{nota10} nota(s) de R$ 10,00')
 print(f'{nota5} nota(s) de R$ 5,00')
 print(f'{nota2} nota(s) de R$ 2,00')
 print(f'{nota1} nota(s) de R$ 1,00')


main()
