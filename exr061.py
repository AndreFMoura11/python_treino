print('PA 2')

primeiro =int(input('Digite o numero:'))
razao= int(input('Digite a RAZÃO:'))


termo = primeiro
cont = 1 # CONTADOR DOS TERMOS


while cont <=10:
    print('{} > '.format(termo),end='')
    cont += 1
    termo = termo + razao


