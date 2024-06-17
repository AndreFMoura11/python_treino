print('PA')
#PA = conta de zero até 10 pulando de 2 em 2       Onde o primeiro termo é 0 e o segundo é 2

primeiro =int(input('Digite o numero:'))
razao= int(input('Digite a RAZÃO:'))
decimo= primeiro + (10-1)* razao # Essa formula para controlar quais numeros eu quero no caso seria os numeros até o 10

for pa in range(primeiro,decimo,razao):
    print('{}'.format(pa),end='--->')
print('=== FIM DO PROGRAMA===')


    