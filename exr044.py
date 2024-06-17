print('Produto valor a ser pago')
#INPUTS

valor=float(input('Qual o valor do produto?:'))
vp=str(input('A vista ou parcelado ?:')).strip()
mododepagamento=str(input('Dinheiro ou cartão ?:')).strip()

 #Cartão Parcelamento
if 'PARCELADO' in vp.upper():
    parcelas=int(input('Quantas parcelas:?'))
    #2X CARTAO
    if parcelas >= 1 and parcelas <= 2 :
        valorpago=float (valor/parcelas)
        print('Parcelado em {} no {} fica no valor de {} por mes'.format(parcelas,mododepagamento,valorpago))
    #3x =>
    elif parcelas >= 3:
        #20% JUROS
        valorparcela = float (valor/parcelas)
        valorpago2 = float ((20/100)*valorparcela)+valorparcela
        print('Parcelado em {} no {} fica no valor de {} por mes'.format(parcelas,mododepagamento,valorpago2))

 #VISTA , CARTAO E DINHEIRO
elif 'VISTA' in vp.upper():
    if 'CARTAO' in mododepagamento.upper() or 'CARTÃO' in mododepagamento.upper() :
     desconto=(5/100)*valor
     valorpagar = valor - desconto
     print('A vista no Cartão ficara :{}'.format(valorpagar))

    elif  'DINHEIRO' in mododepagamento.upper():
        desconto= float((10/100)*valor)
        valorpagar = float(valor-desconto)
        print('No Dinheiro a vista fica :{}'.format(valorpagar))
print('=== FIM DO PROGRAMA ===')












