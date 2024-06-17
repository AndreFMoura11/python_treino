import random
import math
numero=int(input('De 1 a 10 em Qual numero estou pensando ?'))

al= math.ceil(10*random.random())  # ceil arredonda para cima
if numero == al:
    print('Você Acertou o numero é {}'.format(al))
else :
    print('Você Errou !\n O numero é:{}\nMais sorte da Proxima vez'.format(al))

print('Obrigado por Jogar !!!' )
