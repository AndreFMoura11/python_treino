print('Maior idade')
from datetime import datetime
hoje = datetime.today()
ano = hoje.year

anos_nascimentos = []  # Criar a lista fora do laço

# lISTA DAS PERGUNTAS INPUTS   para criar as perguntas com a numeração personalizada tambem
for pessoas in range(1,7+1):
    anos_nascimentos_input = int(input('E quem ano você nasceu pessoa {}?:'.format(pessoas)))
    anos_nascimentos.append(anos_nascimentos_input) # É A VARIAVEL DA LISTA
    # append()  para colocar os inputs da
    # outra variavel dentro da lista ja criada fora do laço

for anos_nascimentos_input in anos_nascimentos:
    # Pega da Variavel do input   "DENTRO" da variavel da LISTA

    idades_pessoas = ano - anos_nascimentos_input
    if idades_pessoas >= 18:
        print('\033[32mMaior de Idade\033[m ',end='') # colocar sempre o envio de cores completo pois em alguns terminais pode dar erro
    elif idades_pessoas < 18:
        print('\033[31mMenor de Idade\033[m ',end='')
    print('Com a idade de :{} '.format(idades_pessoas))














