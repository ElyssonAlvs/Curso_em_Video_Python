from time import sleep
import math # Biblioteca que será usada
ang = float(input('\033[4;34mDigite um ângulo e mostreremos seu seno,cosseno e tangente \033[m :  ')) # Digite o ângulo que será mostrado seu seno , cosseno , tangente
sen = math.sin(math.radians(ang)) # Mostrará o valor do seno , mas em radianos ([math.radians()]) , para transformar em radianos
cos = math.cos(math.radians(ang)) # Mostrará o valor de cosseno , mas em radianos ([math.radians]) , para transformar em radianos
tang = math.tan(math.radians(ang)) # Mostrará o valor de tangente , mas em radianos ([math.radians]) , para transformar em radianos
print('\033[1;30mCALCULANDO.....\033[m')
sleep(2)
print('O ângulo \033[1;34m{}°\033[m têm seno valendo \033[1;31m{:.1f}\033[m,cosseno igual a \033[1;32m{:.1f}\033[m e tangente \033[1;33m{:.1f}\033[m'.format(ang, sen, cos, tang))
# Mostrará os valores seno , cosseno , tangente em radianos
print('*' * 74)
ang = float(input('\033[4;34mDigite um ângulo e mostreremos seu seno,cosseno e tangente \033[m :  ')) # Digite o ângulo que será mostrado seu seno , cosseno , tangente
sen = math.sin(ang) # Mostrará o valor do seno , mas em inteiros
cos = math.cos(ang) # Mostrará o valor de cosseno , mas em inteiro
tang = math.tan(ang) # Mostrará o valor de tangente , mas em inteiro
print('\033[1;30mCALCULANDO.....\033[m')
sleep(2) # time for 2 second
print('O ângulo \033[1;34m{}°\033[m têm seno valendo \033[1;31m{:.1f}\033[m,cosseno igual a \033[1;32m{:.1f}\033[m e tangente \033[1;33m{:.1f}\033[m'.format(ang, sen, cos, tang))
# Mostrará os valores seno , cosseno , tangente em inteiro 