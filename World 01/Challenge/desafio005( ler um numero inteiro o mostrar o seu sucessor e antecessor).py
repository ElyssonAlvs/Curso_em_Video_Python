n = int(input('\033[4;32mDigite um número\033[m:')) # Digite o número , e será mostrado o seu antecessor e antecessor
ant = n -1 # Operação para descobrir o antecessor do número listado
suc = n +1 # Operação para descobrir o sucessor do número listado
print('Seu antecessor é \033[4;33m{}\033[m e seu sucessor é \033[4;36m{}\033[m '.format(ant,suc )) # Forma de realizar ¹
#print('seu antecessor é {} e seu sucessor é {} '.format((n+1), (n-1))) Forma de realizar ²