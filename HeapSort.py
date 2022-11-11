# Heap Sort

def heapify(palavra, n, i): 
    maior = i  
    l = 2 * i + 1      
    r = 2 * i + 2     

    if l < n and palavra[i] < palavra[l]: 
        maior = l 
  

    if r < n and palavra[maior] < palavra[r]: 
        maior = r 
  
    if maior != i: 
        palavra[i],palavra[maior] = palavra[maior],palavra[i]  
  
        heapify(palavra, n, maior) 
  
def heapSort(palavra): 
    n = len(palavra) 
  

    for i in range(n, -1, -1): 
        heapify(palavra, n, i) 
  
    for i in range(n-1, 0, -1): 
        palavra[i], palavra[0] = palavra[0], palavra[i]  
        heapify(palavra, i, 0) 
  
palavra = list(input('Digite a sua String > ').split())
heapSort(palavra) 
n = len(palavra) 

for i in range(n): 
    print (palavra[i])