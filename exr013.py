print('Reajuste Salarial')
s=float(input('Digite o seu salario atual:'))
r=s+(s*15/100)
print('Seu salario atual de R${} com aumento de 15% fica:R${:.2f}'.format(s,r))
