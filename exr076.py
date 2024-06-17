print('Produtos')


# produtos = ('Banana','Pera','Maça','Azeite ')

 # preço = ('R$22,00','R$10,00','R$5,00','R$3,00')

 # tupla = (produtos ,preço )

tupla = ('Banana','Pera','Maça','Azeite',22.00,10.00,5.00,3.00)


for c in tupla: 
    if isinstance(c,str):  
        produtos = c 
        print(produtos,end=" ")
    else:   
        print(c,end=" ")
        
impressao = ("""
             PRODUTOS
             
             """)