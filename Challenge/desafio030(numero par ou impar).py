from time import sleep # "Pacote" (time) que será utiliza junto com a função ( sleep)
print('\033[1;4;30m-----------------------------------------------\033[m')
n = int(input('\033[mQual o número q será analisado\033[m ? ')) # Informar qual número será analisado pelo computador
print('ANALISANDO NÚMERO INFORMADO......')
sleep(3) # Função em execução
# Início da Estrutura Condicional
if n % 2 == 0 :
    print('O NÚMERO É \033[4;31mPAR\033[m !')
else :
    print('O NÚMERO É \033[4;34mÍMPAR\033[m !')
# Final da Estrutura Condiconal
print('-----------------------------------------------')

print('+' * 50)

número = int(input('\033[mMe diga um número qualquer\033[m : '))
resultado = número % 2
print('O resultado foi {} '.format(resultado))
if resultado == 0 :
    print('O número {} é PAR '.format(número))
else:
    print('O número {} é ÍMPAR'.format(número)) 