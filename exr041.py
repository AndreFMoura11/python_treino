print('Confederação Nacional de Natação \n')
print('Limite minimo de idade 9 anos\n')
ano=int(input('Qua o ano que você nasceu?:'))

idade= 2023 - ano

#NAO PRECIASA COLOCAR AS DUAS CONDIÇOES
if idade >= 9 and idade < 14:
    print('Categoria MIRIM')
elif idade >= 14 and idade < 19:
    print('Categoria INFANTIL')
elif idade >= 19 and idade < 20:
    print('Categoria JUNIOR')
elif idade > 19 and idade >= 20 :
    print('Categoria Senior')
elif idade >= 20 :
    print('Categoria Senior')
print('=== FIM DO PROGRAMA ===')
