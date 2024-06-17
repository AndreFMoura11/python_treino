print('Sequencia de Fibonacci')

num = int(input('Digite um numero:'))



ter1 = 0  # Termos tradicionais   0 e 1 
ter2 = 1  # Acho que é porque na sequenca de fibonacci os 2 primeiros sao 0 e 1 , nao tem como trasnformar 0 + 0 em 1 quando colocando em um laço para calculo imagino

print('{} > {} '.format(ter1,ter2),end='') # A questao de poder colocar um print junto mas separado de outro print 

cont = 3 # Geralmente atrelado ao uso do while   # E começa a contar o no 3 

while cont <= num: # Num determina a quantidade que vai mostrar portanto é o limite
    ter3 = ter1 + ter2
    print('> {}'.format(ter3),end='') # Print colocando separado do print do calculo com condição , ambos se juntam no final
    ter1 = ter2  # O que estava dentro da variavel é substituido
    ter2 = ter3  # Faz como se as variaveis tivessem se mechendo sendo substituidas pelos os resultados e abriando espaço para a nova no termo 3 com o resultando do calculo da formula
    cont += 1 # Contandor atrelado ao while para controle de vezes que sera executado 
    
    
print('\nFIM DO PROGRAMA')
