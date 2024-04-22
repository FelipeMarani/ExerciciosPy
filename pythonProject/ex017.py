import math
cO, cA = map(float, input('digite a medida do Cateto Oposto e do Cateto Adjacente do triângulo Retangulo: ').split())
if cO <= 0  or cA <=0:
    print('Impossivel calcular')
else:
    result = math.hypot(cO, cA)
    print('O comprimento da hipotenusa é de {:.2f}'.format(result))