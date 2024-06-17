print('Informativo de alistamento')

nome=(input('Qual o seu nome ?:'))
ano=int(input('Qual foi o ano que você nasceu ?:'))

# Não sei ainda como que faz para o ano ficar atualizando
idade = 2023 - ano

if  idade > 18 :
    tempofalta=idade - 18
    print('{} você já esta atrasado para fazer o alistamento a :{} anos'.format(nome,tempofalta))
elif idade < 18:
    tempoacima= idade - 18
    positivo=abs(tempoacima)
    print('{} vá se alistar urgente'.format(nome))

elif idade == 18:
    print('{} Vá se alistar'.format(nome))
print('=== FIM DO PROGRAMA ===')

