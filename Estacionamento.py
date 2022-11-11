

hi, mi = input().split(':')
hf, mf = input().split(':')

hi = int(hi)
hf = int(hf)
mi = int(mi)
mf = int(mf)

total_i = hi * 60 + mi
total_f = hf * 60 + mf

geral = total_f - total_i

if geral > 180:
    print('Valor a pagar: R$ 5,00')

elif geral > 120:
    print('Valor a pagar: R$ 4,00')

elif geral > 60:
    print('Valor a pagar: R$ 3,00')

elif geral > 15:
    print('Valor a pagar: R$ 2,00')

else:
    print('Estacionamento Grátis')
