

# Capta a informaçao dos inputs e processa os dados no laço , ai pega uma variavel do lado de fora do laço e
# E envia a informação para ela

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print('---- {} Pessoa ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Genero [M/F]: ')).strip()
    somaidade += idade


    # Tratar as Informação

    if p == 1 and genero in 'Mm' :  # colocou ja a condiçao escolhendo o primeiro laço e a condiçao para tratar a informaçao
        maioridadehomem = idade
        nomevelho = nome

    if genero in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

# Usando das variaveis fora do laço para mostrar
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

























