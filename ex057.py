print('Teste de palavras')

genero = str(input('Qual o seu genero ? :')).strip().upper() # Variavel input fora do laço
while genero not in 'MmFf':    #Not in  #Enquanto
    genero = str(input('Dados invalidos. Por favor , informe seu genero: ')).strip().upper()[0]  # vai pegar so a primeira letra ( escolhendo pelo o numero a localizaçao na string)
print('Genero {} Registrado com sucesso'.format(genero))







