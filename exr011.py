print('Pintando a parede')
larg=float(input('Qual a largura da sua parede?'))
altura=float(input('Qual a altura da sua parede?'))
area=larg*altura
tinta=2
rtinta=area/tinta
print('A area de sua parede:{}m2\nTinta necessaria para pintar a sua parede:{}Litros'.format(area,rtinta))