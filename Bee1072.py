

numb = int(input())

cont = 0

cont1 = 0
cont2 = 0

while cont < numb:

    numb1 = int(input())

    cont = cont +1

    if numb1 >= 10 and numb1 <= 20:

        cont1 = cont1 + 1

    else:

        cont2 = cont2 + 1
    


print(f'{cont1} in')
print(f'{cont2} out')

