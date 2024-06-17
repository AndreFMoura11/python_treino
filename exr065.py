print('Maior e Menor Valores')

#sn = str(input('Quer continuar [s/n]:')).upper().strip()

sn = 's' # colocar ja travado a resposta para a fase de testes sempre colocar algusn nao funcionam
cont = 0
soma = 0
maior = 0
menor = 0

while sn in 'Ss':   
    num = int (input('Digite um numero:'))
    sn = str(input('Quer continuar [s/n]:')).upper().strip()
    
    cont += 1
    # Tratamento de Dados  
    # Maior e Menor
    if cont == 1:             #Memorizar antes do # o usar o CONT para controlar a quantidade de vezes que ocorreu
        maior = menor = num
    else:   
        if num > maior: 
            maior = num
        if num < menor: 
            menor = num
    # Media
    soma += num
media = soma / cont # se quiser colocar algo embaixo , mas ainda dentro da chave logica precisa ser antes disso pois pode dar erro

# Print fora caixa logica    
print("""Soma: {} Cont:{} 
        sn: {} media: {} num: {}
        Maior:{} Menor{}""".format(soma,cont,sn,media,num,maior,menor))


# Tratamento de dados funciona fora do laço pelo o que eu vi 
# Perguntas se colocar logo dentro do laço quando nao precisa separar algum dado especifico

#Tratamento de Dados

#Media
    


print('=== FIM DO PROGRAMA ===')
