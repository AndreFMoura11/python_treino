print('Cinco numeros aleatorios')

from random import randint

numeros = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))


cont= 0
maior= 0
menor = 0

print("""
      Tupla:{}
      Maior{}
      Menor{}
      """.format(numeros , max(numeros), min(numeros)))