print('Calculador de Medias')

nota1=float(input('Digite o valor da sua primeira nota:'))
nota2=float(input('Digite o valor da sua segunda nota:'))

media = float((nota1 + nota2)/2)

if media <= 5.0 :
    print('REPROVADO')

elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')

elif media >= 7.0:
    print('APROVADO')

print('Vá estudar')


