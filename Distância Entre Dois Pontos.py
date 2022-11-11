# Atividade do beecrowd 1015
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, 
# p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, 
# mostrando 4 casas decimais após a vírgula, segundo a fórmula:

import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1,y1 = linha1
x2,y2 = linha2

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %distancia)