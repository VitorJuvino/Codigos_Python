
# Leia um valor inteiro X. Em seguida apresente 
# os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

numb = int(input())

cont=0

while cont<6:

    if numb%2!=0:
        
        print(numb)

        cont+=1
    numb+=1