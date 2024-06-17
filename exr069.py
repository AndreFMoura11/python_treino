print('Varias Pessoas A B C ')

p = 0
h = 0
m = 0 
sn =' '
while True:
    idade = int (input('Qual a sua Idade?:'))
    genero = str(input('Qual o seu genero [M/F]:')).upper().strip()
    
    # Tratamento de Dados
    if idade >= 18: 
        p += 1
    if genero in 'M' or genero in 'HOMEM':   
        h += 1
    if genero in 'F' and idade < 20:  
        m += 1 
    
    sn = str (input('Continuar[S/N]?:')).upper().strip()    
    if sn in 'N':
        break
        
            
print("""
      Pessoas com mais de 18 anos:{}
      Homens cadastrados:{}
      Mulheres com menos de 20 anos:{}
      """.format(p,h,m))
