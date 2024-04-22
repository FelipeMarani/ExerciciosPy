import math
ang = float(input('Digite um angulo qualquer positivo:'))
if ang <= 0:
    print('Não é possivel calcular')
else:
    cos = math.cos(ang)
    sen = math.sin(ang)
    tang = math.tan(ang)
print('O cosseno do angulo {:.2f} é {:.2f}, tem seno em {:.2f} e tangente em {:.2f}'.format(ang, cos, sen, tang))