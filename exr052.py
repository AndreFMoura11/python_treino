print('Numero primo')

num= int(input('Digite um numero:'))
tot= 0
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m',end='')
    else:
        print('\033[31m',end='')
    print('{}'.format(c),end='')

print('\n\033[m0 numero {} foi divisivel {} vezes '.format(num,tot))

if tot == 2:
    print('E por isso ele é PRIMO')

    print('E por isso ele nao é ´PRIMO')