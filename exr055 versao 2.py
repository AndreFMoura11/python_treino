maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Peso da pessoa {}:'.format(p)))
    # Tratamento das informaçoes recebidas

    if p == 1:         # Aqui ele pega a primeira volta do laço
        maior = peso   # preenche as variaveis se so tiver 7 , o numero maior e menor sera o 7
        menor = peso   # Essa é uma condiçao somente para o primeiro laço
    else:
        if peso > maior:    # aqui ele vai executar o resto dos laços subsequentes
            maior = peso    # Vai comparar tudo e substituir na variavel caso encontre um maior ou menor
        if peso < menor:    # que ja esta preenchida pelo o valor do primeiro laço
            menor = peso

print('O Maior:{} o Menor:{}'.format(maior,menor))

