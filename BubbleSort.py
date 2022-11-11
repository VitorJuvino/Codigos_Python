
palavra = list(input('Digite a sua String > ').lower())
tam_palavra = len(palavra)

# bubble sort
for i in range(tam_palavra):
    troca = False
    for j in range(1, tam_palavra - i):
        if palavra[j] < palavra[j - 1]:
            palavra[j], palavra[j - 1] = palavra[j - 1], palavra[j]
            troca = True
    if not troca:
        break

print(palavra)