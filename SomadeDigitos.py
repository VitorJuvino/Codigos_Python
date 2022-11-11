
n = int(input('>'))

soma = 0
    
while n:
    soma = soma + n % 10 
    n //= 10 

print(soma)