print('Break Varios numeros')

soma = 0
cont = 0

while True: 
    
    num = int(input(' 1 Digite o numero:'))
    
    if  num == 999: # Ele colocou entre os tratamentos de dados 
        break     # Precisa para fluxo do laço ( e excluindo a ultimo retorno ja que ele era o condicional)
                  # Antes de se fazer o calculo , entao ele ira usar os que já
    soma += num   # Foram acumulados e fara as somas e formulas embaixo
    cont += 1
print('Soma:{} Quantidade:{}'.format(soma,cont))