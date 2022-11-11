# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
# o valor que recebe por hora e calcula o salário desse funcionário. 
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

numero_funcionarios = int(input())
horas_trabalhadas = int(input())
valor_por_horas_tra = float(input())

salario = float(horas_trabalhadas * valor_por_horas_tra)

print("NUMBER = %d" %numero_funcionarios)
print("SALARY = U$ %0.2f" %salario)