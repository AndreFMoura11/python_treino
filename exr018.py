print('Seno Cosseno e tangente')
import math
angulo=float(input('Digite o seu angulo:'))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print('Triangulo Retangulo\nAngulo:{}\nSeno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(angulo,seno,cosseno,tangente))