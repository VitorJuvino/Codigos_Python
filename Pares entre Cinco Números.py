# URI1065

# criando a lista
lista = []
for i in range(5):
    # recebendo os valores
    n = int(input())
    # adicionando os valores da variavel(n) para a lsta(a) com o append
    lista.append(int(n))

# criando um contador
contador = 0

for x in range(5):
    if lista[x] % 2 == 0:
        contador += 1
print(contador, "valores pares")