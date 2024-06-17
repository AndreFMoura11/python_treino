print('Aumento de salario')

salario=float(input('Qual é o valor do seu salario?:'))

if salario > 1250:
    salarior1 =float( salario*10/100+salario)
    print('\nSeu salario de R${} ira aumentar em 10%\n Para R$:{}'.format(salario,salarior1))



elif salario <= 1250:
    salarior2= float(salario*15/100+salario)
    print('Seu salario de R${} ira aumentar em 15%\nPara R$:{}'.format(salario,salarior2))
print('Fim do programa')
