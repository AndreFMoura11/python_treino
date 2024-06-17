print('IMC')

nome=input('Qual o seu nome?:')
peso=float(input('Quantos Kg você pesa ? :'))
altura=float(input('Qual a sua altura em metros ? :'))

#NAO SEI A FORMULA , NAO ENTENDI
imc2=float(peso / (altura**2))
imc3=float(imc2/peso)

if imc >= 0 and imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc >= 40 :
    print('VOCÊ ESTA FRITO MEU AMIGO')
print('=== FIM DO PROGRAMA ===')
