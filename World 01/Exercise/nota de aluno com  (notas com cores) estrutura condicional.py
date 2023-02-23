import emoji # Biblioteca para usar a ferramenta emoji
from time import sleep # Biblioteca para usar a ferramenta sleep
nota01 =float(input('\033[1;34mA primeira nota do aluno  \033[m :')) # Digite o número para reallizar sua média ¹
nota02 =float(input('\033[1;37mA segunda nota do aluno  \033[m :')) # Digite o número para realizar a média ²
m = (nota01+nota02)/2 # Equação para realizar a média dos número informados
limite = 6.0
print('Sendo a média igual a {}{}{} então...'.format( '\033[1;33m' , limite , '\033[m' )) # Média mínima que o usuário tem que alcançar para passar na prova
sleep(2)
if m >= 6.0 :
    legal = emoji.emojize(':thumbsup:', use_aliases=True)
    print('Sua nota foi {}{}{} , você alcançou a média limite {}'.format('\033[1;32m' , m , '\033[m' , legal ))
    # Se a média do usuário for acima da 'média' , ele passou na prova
else :
    triste = emoji.emojize(':-1:', use_aliases=True)
    print('Sua nota foi {}{}{} , você não alcançou a média limite , precisa melhorar {}'.format('\033[1;31m' , m , '\033[m' , triste))
    # Senão , ele não alcançou a 'média' portanto precisa melhorar