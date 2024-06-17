print('Super Baratão')

total = 0
cont_produto_mais = 0 
nome_produto = ' '
sn = ' '
total_valor= 0 
cont = 0
produto_menor_valor = 0
produto_maior_valor = 0 
produto_menor_nome = ' '
while True: 
    produto =str(input('Nome do produto:')).strip().upper()
    preço = float(input('Qual o valor:'))
    cont += 1
    # Tratamento de Dados
    
    # A
    total_valor += preço
    # B
    if preço > 1000:    
        cont_produto_mais += 1
    # C                                          # //// IMPORTANTE
    if cont ==1 or preço < produto_menor_valor:  # condiçao de cont ==1 mesmo e a novidade preço(valor) menor q uma variavel q ja estava com valor zero antes q seria prechida dentro do laço
        produto_menor_valor = preço
        produto_menor_nome = produto      
    sn = str(input('Quer continuar[S/N]')).strip().upper()[0]

    
    
    if sn in 'N':
        break
print("""
      Total gasto:{}
      Quantos produtos custam mais de R$1000:{}
      Produto mais barato é : {}
      
      """.format(total_valor,cont_produto_mais,produto_menor_nome))
        