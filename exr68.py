print('Jogo do Par ou Impar while e break\n')

from random import randint 

cont = 0

while True: 
  jogador = int(input('Diga um valor: '))
  maquina_num = randint(0,10)  
  '''
A função randint é uma função da biblioteca random em Python. Ela é usada para gerar números inteiros aleatórios dentro de um intervalo especificado.

A assinatura da função randint é a seguinte:

python
Copy code
random.randint(a, b)
Onde:

a é o limite inferior do intervalo (inclusive).
b é o limite superior do intervalo (inclusive).
'''  
  total = jogador + maquina_num
  tipo= ' '   # SEMPRE DEIXE UM ESPAÇO ENTRE AS ASPAS 
  
  while tipo not in 'PI': 
    tipo = str(input('[P/i] ?')).upper().strip()[0]
 # Ele criou fora para colocar dentro de outro laço infinito
 # O 0 é para ele pegar somente a primeira letra da palavra

  print('Você jogou {} e o computador {} Total de {}'.format(jogador,maquina_num,total))
  # Colocadno o print fora do laço 
  
  # Tratamento de Dados
  
  # Ao inves de criar varios IF para varias possibilidades vc criar blocos de comando
  
  # //// Importante   Condiçoes usando uma variavel vazia e para iniciar a condiçao ele usa NOT IN ( naturalmente nao tera nada)
  if tipo not in 'P':        # Condiçoes de tipo ja transformadas em caixas logicas
    if total / 2 == 0 : 
      print('GANHOU')
      cont += 1          # Contador 
    else: 
      print('PERDEU')    # Quando perde o jogo acaba interropendo o laço
      break
  elif tipo  not in 'I':     # Primeiras letras em maiusculo 
    if total / 2 == 1:   # Para saber se é impar so colocar  /2 == 1 
      print('GANHOU')
    else:   
      print('PERDEU')
      break
  print('Vamos jogarr novamente')
  
   # ta dando errado , o acertei pa 10 + 10 = 20  e ele isse q eu perdi