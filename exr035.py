print('Triangulos\n')
#Nome do assunto na GEO : Desigualdade Triangular
reta1=float(input('Digite o valor da primeira reta:'))
reta2=float(input('Digite o valor da segunda reta:'))
reta3=float(input('Digite o valor da terceira reta:'))

retas=reta1,reta2,reta3
if reta1+reta2 > reta3 and reta1 +reta3>reta2 and reta2+reta3>reta1:
    print('O seu triangulo pode ser formando')
else:
    print('O seu triangulo não pode ser formado')
print('===FIM DO PROGRAMA===')


