

numb1, numb2, sinal = input().split()

numb1 = int(numb1)
numb2 = int(numb2)
sinal = str(sinal)


if sinal == '+':

    resultado = numb1 + numb2
    print(resultado)

elif numb2 < numb1 and sinal == '-':

    resultado = numb1 - numb2
    print(resultado)

elif sinal == '*':

    resultado = numb1 * numb2
    print(resultado)

elif numb2 < numb1 and sinal == '/':

    resultado = numb1 // numb2
    print(resultado)

else:
    print('')