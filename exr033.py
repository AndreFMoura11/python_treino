print('Qual o maior e Qual o menor ?')
num1=float(input('Digite o primeiro numero:'))
num2=float(input('Digite o segundo numero:'))
num3=float(input('Digite o terceiro numero:'))

numeros=[num1,num2,num3]

if num1 > num2 and num1 > num3:
    print('Numero 1 {} é o maior'.format(num1))
elif num2 > num1 and num2 > num3:
    print('Numero 2 {} é maior'.format(num2))
else:
    print('Numero 3 {} é o maior'.format(num3))
print('oObrigando por usar')



