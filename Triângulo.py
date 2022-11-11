
# Atividade Triângulo do beecrowd

s = input().split()

a, b, c = s

a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format(((a + b) / 2) * c))