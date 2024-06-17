print('Alunos Ordem Sortiada')
from random import shuffle
al1=input('Aluno 01:')
al2=input('Aluno 02:')
al3=input('Aluno 03:')
al4=input('Aluno 04:')
alunos=[al1,al2,al3,al4]
r=shuffle(alunos)
print('O aluno sorteado foi {}'.format(r))
print(alunos)