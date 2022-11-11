# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, 
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
#  Após, calcule e mostre o valor a ser pago.

cx, qx, vx = input().split()
cy, qy, vy = input().split()
c1 = int(cx)
q1 = int(qx)
v1 = float(vx)
c2 = int(cy)
q2 = int(qy)
v2 = float(vy)
vp = (q1 * v1) + (q2 * v2)
print(f'VALOR A PAGAR: R$ {vp:.2f}')
