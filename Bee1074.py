

quant = int(input())


for i in range(quant):

    numb = int(input())

    if numb == 0:
        print('NULL')

    elif numb % 2 == 0:
        
        if numb < 0:
            print('EVEN NEGATIVE')
        else:
            print('EVEN POSITIVE')
    elif numb % 2 != 0:
        if numb < 0:
            print('ODD NEGATIVE')
        else:
            print('ODD POSITIVE')
    
    
