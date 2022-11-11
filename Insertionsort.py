# Insertion Sort
def insertionsort(A):
 #iniciamos o loop no segundo elemento (índice 1) já que o primeiro item já está ordenado

    for j in range(1,len(A)):
        key = A[j] #O próximo item que vamos inserir na seção ordenada do array

        i = j-1 #o último item que vamos comparar
        #agora continuamos movendo a chave de volta enquanto ela for menor que o último item do array
        while (i > -1) and key < A[i]: #if i == -1 significa que esta chave pertence ao início
            A[i+1]=A[i] #mova o último objeto comparado um passo à frente para abrir espaço para a chave
            i=i-1 #observe o próximo item para a próxima vez.
        #okay i não é maior que a chave significa que a chave pertence a i+1
        A[i+1] = key
    return A



if __name__=="__main__":
    x = list(input("Digite ->> ")) 
    insertionsort(x)
    print (x)