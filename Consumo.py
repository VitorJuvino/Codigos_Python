# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) 
# e o total de combustível gasto (em litros).

def main():
    x = int(input())
    y = float(input())

    consumo = x / y
    print(f'{consumo:.3f} km/l')

main()
