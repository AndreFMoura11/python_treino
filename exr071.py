print('Caixa Eletronico')


cont = 0
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0
valor_final = 0 
valor_sacar = 0
while True: 
    valor_sacar = int(input('Qual o valor deseja sacar?:R$'))
    
    c50 = 50
    c20 = 20
    c10 = 10
    c1 = 1

    # 50
    while valor_sacar >= 50:    
        valor_final += 50
        cont_50 += 1
        if valor_final > valor_sacar:   
            valor_final -= 50
            cont_50 -= 1
            break
    print(' 2 Deu certo:{} \n cont:{}'.format(valor_final,cont_50))
    # 20
    while valor_final < valor_sacar:    
        valor_final += 20
        cont_20 += 1
        if valor_final > valor_sacar:   
            valor_final -= 20
            cont_20 -= 1
            break
    # 10
    while valor_final < valor_sacar:
        valor_final += 10
        cont_10 += 1
        if valor_final > valor_sacar:
            valor_final -= 10
            cont_10 -= 1
            break
    # 1
    while valor_final < valor_sacar:
        valor_final += 1
        cont_1 += 1
        if valor_final > valor_sacar:
            valor_final -= 1
            cont_10 -= 1
            break
                
        
        
        print(""" 
            Valor Final:{}
            Notas de 50:{}
            Notas de 20:{}
            Notas de 10:{}
            Notas de 1:{}""".format(valor_final,cont_50,cont_20,cont_10,cont_1))
        
    if valor_final == valor_sacar:  
        break
    
    

    
    