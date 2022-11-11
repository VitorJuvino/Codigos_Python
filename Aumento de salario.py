
# Beecrowd 1048

import os

os.system('cls')

x = float(input())

def Aumento_salario():

    if x >= 0 and x <= 400.00:
        rg = x * 15 / 100
        ns = x + rg
        
        print(f'Novo salario: {ns:.2f}')
        print(f'Reajuste ganho: {rg:.2f}')
        print(f'Em percentual: 15 %')

    if x >= 400.01 and x <= 800.00:
        rg = x * 12 / 100
        ns = x + rg
        
        print(f'Novo salario: {ns:.2f}')
        print(f'Reajuste ganho: {rg:.2f}')
        print(f'Em percentual: 12 %')

    if x >= 800.01 and x <= 1200.00:
        rg = x * 10 / 100
        ns = x + rg
        
        print(f'Novo salario: {ns:.2f}')
        print(f'Reajuste ganho: {rg:.2f}')
        print(f'Em percentual: 10 %')

    if x >= 1200.01 and x <= 2000.00:
        rg = x * 7 / 100
        ns = x + rg
        
        print(f'Novo salario: {ns:.2f}')
        print(f'Reajuste ganho: {rg:.2f}')
        print(f'Em percentual: 7 %')

    if x >= 2000.01:
        rg = x * 4 / 100
        ns = x + rg
        
        print(f'Novo salario: {ns:.2f}')
        print(f'Reajuste ganho: {rg:.2f}')
        print(f'Em percentual: 4 %')


Aumento_salario()