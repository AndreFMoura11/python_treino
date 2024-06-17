print('Distancia de uma viagem')

km=float(input('Qual a distancia da viagem ?:'))

if km < 200:
    kmr=km*0.50
    print('\nValor da passagem com a distancia de :{}Km\nFica no valor de :R${}'.format(km,kmr))
else:
    kmr2=km*0.45
    print('\nValor da passagem com a distancia de :{}Km\nFica no valor de :R${}'.format(km, kmr2))

print('Aproveite a Viagem')
