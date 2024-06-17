print('PA 2')

primeiro =int(input('Digite o numero:'))
razao= int(input('Digite a RAZÃO:'))

termo = primeiro    
cont = 1
total = 0
mais = 10 # Simulando numero
while mais != 0:     # LIMITA A QUANTIDADE DE VEZES QUE ELE VAI FAZER E MOSTRA O CALCULO (EXECUTAR O QUE ESTA DENTRO) USANDO A VARIAVEL CONT PARA ISSO 
    total = total + mais
    while cont <= total:    
        print('{} > '.format(termo),end='')
        termo += razao
        cont += 1   
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('FIM')

        
    





