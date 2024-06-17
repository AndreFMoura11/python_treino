print('Sorteio item')
import random
print('Quais são as suas 3 comidas favoritas?')
com1=input('Comida 1:')
com2=input('Comida 2:')
com3=input('comida 3:')
com4=input('comida 4:')
comidas=[com1,com2,com3,com4]
f=random.choice(comidas)
print('Comida sorteada:{}'.format(f))


