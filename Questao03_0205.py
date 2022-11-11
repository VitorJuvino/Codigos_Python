

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if a == b and a == c and b == c:
    print('Empate entre empresas')

elif a < b and a < c:
    print('A empresa A venceu a licitacao')

elif b < a and b < c:
    print('A empresa B venceu a licitacao')

elif c < a and c < b:
    print('A empresa C venceu a licitacao')


else:
    print('')

