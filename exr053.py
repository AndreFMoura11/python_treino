print('Polindromoscopio')

frase = str(input('Digite uma frase:')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)
inverso= junto[::-1]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A palavra digitada não é um palindromo')
