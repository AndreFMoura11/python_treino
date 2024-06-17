print('Desafio 59')

num1=float(input('Digite o primeiro numero:'))
num2=float(input('Digite o segundo numero:'))

menu=str(input("""
======= MENU =======
Soma [1]
Multi[2]
Maior[3]
Novos Numeros[4]
Sair Do Programa [5]
"""))

#Soma
if menu == '1':
    numr= num1 + num2
    print('A SOMA DE {} E {} É DE :{}'.format(num1,num2,numr))
# Multiplicação
elif menu == '2':
    numr = num1 * num2
    print('A Multiplicação de {} e {} é de :{}'.format(num1,num2,numr))
#Maior
elif menu == '3':
    if num1 > num2:
        print('O numero maior:{}'.format(num1))
    else:
        print('O numero maior:{}'.format(num2))
#Novos numeros
elif menu == '4':
    print('ARQUIVO VAZIO')

elif menu =='5':
    print('===== FIM DO PROGRAMA =====')


