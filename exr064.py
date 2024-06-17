print('Tratando Varios Numeros')

num = cont = soma = 0      # Precisa para criar as variaveis fora do laço , pois ele nao iria aceitar caso existisem somente no laço pois tecnicamente ainda iria ser gerado
num = int(input('Digite um numero  (FORA DO LAÇO) [999 para parar]'))  # Colocando a mesma pergunta aqui fora e no laço , faz com que quando ele coloque 999 no input q esta dentro do laço
                                                       # ele não some e sai automaticamente do laço 
                                                       
while num != 999:   
    soma += num
    cont += 1 
    num = int(input('Digitar um numero [999 para parar]'))  # Segundo input , para separar do 999    # Começa o flag o input por fora e depois termina como ultima linha dentro do laço
print('Você digitou {} numeros e a soam entre eles foi {}.'.format(cont,soma))
