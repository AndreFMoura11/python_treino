import math

print('Emprestimo')
from math import ceil
casa=float(input('Qual o valor da Casa ?:'))
salario=float(input('Qual o valor do seu Salario ?:'))
parcelas=int(input('Quantas vezes ?:'))

pormes= math.ceil(salario / parcelas)

if ( 30 /100)*salario < pormes:
    print('Seu processo foi indeferido')

else:
    print('Parabens vc foi aprovado')
print('===FIM DO PROGRAMA===')

# Errado
