print('Tabuda While e Break')


while True:
     num = int(input('Quer ver a tabuada de qual valor?:'))
     
     # Condição de Parada de laço
     if num < 0:  # Identificar numeros negativos
         break
     # Tratamento de Dados
     for tabuada in range (1,10+1): # Regras copiar no caderno
        resultado_mult = num * tabuada
        print(tabuada,'X',num,'=',resultado_mult)
print('=== FIM DO PROGRAMA ===')