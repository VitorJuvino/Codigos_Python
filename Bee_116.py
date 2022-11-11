

quant = int(input())


for i in range(1, quant + 1):

    numb1, numb2 = map(int,input().split())

    if numb2 == 0:
        print('divisao impossivel')

    if numb2 != 0:
        
        divisao = numb1 / numb2
        print(f'{divisao:.1f}')

