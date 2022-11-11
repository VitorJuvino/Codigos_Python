
palavra = list(input('Digite a sua String > ').split())

# Selection Sort
def selection_sort(a):
	for j in range(len(a)-1):
		minimum = j 
		for i in range(j+1, len(a)): 
			if(a[i]<a[minimum]):
				minimum = i 
		a[j],a[minimum]=a[minimum],a[j] 
	print("after selection sort:")
	print(a)

selection_sort(palavra)