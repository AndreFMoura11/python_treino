print('Leitor e comparador de pesos ')

pesos_pessoas_list = []



for pesos_pessoa_laco in range(1,6):
    pesos_inputs=float (input('Qual o peso da pessoa {}'.format(pesos_pessoa_laco)))

    pesos_pessoas_list.append(pesos_inputs)


peso_maior = max(pesos_pessoas_list)
peso_menor = min(pesos_pessoas_list)
print('O peso Maior:{} e o Menor :{}'.format(peso_maior,peso_menor))

