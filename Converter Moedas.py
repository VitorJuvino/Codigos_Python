# Converter Moedas
# 22-02-22, Vitor

# Solicitar ao usuário o valor de entrada em reais
valor_real = float(input('Qual o valor que deseja converter?'))
# Realizar a conversao para dólares 
valor_dolar = valor_real / 5.06 # cotaçao do dólar em 22-02-22
# imprima na saída o valor convertido
print(f'Pelo cambio atual, R$ {valor_real:.2f}'
f' equivalem a $ {valor_dolar:.2f}')
