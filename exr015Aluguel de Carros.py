print('Carros Alugados')
d=int(input('Quantidade de Dias:'))
km=float(input('Quantidade de KM Rodados:'))
dr=d*60
kmr=km*0.15
t=dr+kmr
print('Carro Alugado\nDias:{}\nKm{}\nTotal a ser pago:R${:.2f}'.format(d,km,t))