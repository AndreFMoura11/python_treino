import random
import math

print('JOGO DA ADIVINHAÇÃO')

quat_erros = 0

numero = int(input('De 0 a 10 em qual numero estou pensando?'))
num_aleatorio = math.ceil(10*random.random())

while numero <= 10 and numero > 0 and numero != num_aleatorio:
    numero = int(input('Você errou , Digite outro numero:'))
    quat_erros = 0 + 1

print('Você acertou o seu numero é :{}\nVocê tentativas {} Vezes'.format(numero,num_aleatorio))
print('FIM DO PROGRAMA')

