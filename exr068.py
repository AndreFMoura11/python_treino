print('Jogo do Par ou Impar while e break')

import random

while True: 
    # Pessoa
    num_pessoa = int(input('Digite um numero:'))
    # Maquina
    num_maquina = random.random()
    
    tipo = str(input('[Impa ou Pá]?:')).upper().strip()
    parar = str(input('Quer continuar [s/n]')).upper().strip()
    
    # Condição do laço interroper
    if parar in 'Nn' or parar in 'NAO' or parar in 'NÃO':
        break
    num = num_pessoa + num_maquina
    
    if num % 2 == 0 and tipo in 'PA' or tipo in 'PÁ':    
        print('GANHOU')
    if num % 2 == 0 and  tipo in 'IMPAR' or tipo in 'ÍMPAR':     #Criar para cada resultado possivel
        print('PERDEU')
    if num % 2 == 0 and tipo in 'IMPAR' or tipo in 'IMPAR': 
        print('GANHOU')