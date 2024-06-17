print('Quanto de Multa')

velcar=float(input('Qual a velociade do carro:'))

multa=float(7*(velcar-80))
if velcar > 80 :
    print('Você Ultrapassou a Velocidade minima de 80Km/h\nSua Multa será de {}'.format(multa))
else:
    print('Velocidade a baixo ou igual a permitida')
print('Fim do Programa')