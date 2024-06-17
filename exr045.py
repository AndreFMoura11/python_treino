print('JOOOOO KEEENNN PÔ!!!')
import random
me=str(input('Você escolhe?:')).strip()

lista=['TESOURA','PEDRA','PAPEL']
pc = random.choice(lista)
print('Escolhi {}'.format(pc))
if 'TESOURA' in pc.upper():

    if 'TESOURA' in me.upper():
        print('EMPATE')
    elif 'PEDRA' in me.upper():
        print('PERDEU')
    elif 'PAPEL' in me.upper():
        print('Venceu')

elif 'PEDRA' in pc.upper():

    if 'TESOURA' in me.upper():
        print('VENCEU')
    elif 'PEDRA' in me.upper():
        print('EMPATE')
    elif 'PAPEL' in me.upper():
        print('PERDEU')
elif 'PAPEL' in pc.upper():
    if 'TESOURA' in me.upper():
        print('PERDEU')
    elif 'PEDRA' in me.upper():
        print('VENCEU')
    elif 'PAPEL' in pc.upper():
        print('EMPATE')
print('== FIM DO PROGRAMA ===')
