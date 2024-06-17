print('VALOR DAS SOMAS DOS PARES')
print('='*40)

soma = 0
contador = 0




for questao in range(1,7):
    num = int(input('Numero {}:'.format(questao)))
    if num % 2 == 0:
        contador = contador + 1
        soma = soma + num
print('Numeros somados {} Contador Numeros Pares :{}'.format(soma,contador))




