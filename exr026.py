
nome=str(input('Digite uma Frase:')).strip().upper()
print('Quantas vezes aparece a letra A:{}'.format(nome.count('A')))
print('Em que posição ela aparece a primeira vez:{}'.format(nome.find('A')))
print('Em que posição ela aparece a ultima vez:{}'.format(nome.rfind('A')))

