print('Triangulos\n')
#Nome do assunto na GEO : Desigualdade Triangular
reta1=float(input('Digite o valor da primeira reta:'))
reta2=float(input('Digite o valor da segunda reta:'))
reta3=float(input('Digite o valor da terceira reta:'))

#Equilatero
if reta1 == reta2 == reta3:
    print('É um triangulo equilatero')
#ISOCELES
elif reta1 == reta2 != reta3 or reta2 == reta3 != reta1 or reta1 == reta3 != reta2:
    print('É um triangulo Isoceles')
#ESCALENO
elif reta1 != reta2 != reta3 :
    print('É um triangulo Escaleno')

print('=== FIM DO PROGRAMA ===')


