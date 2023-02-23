from random import shuffle  # Biblioteca usada com a função que será utillizada
n1 = input('\033[1;30mPrimeiro aluno \033[m:')  # Digite o nome do primeiro aluno
n2 = input('\033[1;31mSegundo aluno\033[m:')  # Digite o nome do segundo aluno
n3 = input('\033[1;32mTerceiro aluno\033[m:')  # Digite o nome do terceiro aluno
n4 = input('\033[1;33mQuarto aluno\033[m:')  # Digite o nome do quarto aluno
lista = [ n1 , n2, n3, n4]  # Lista com o nome dos alunos dados
 #shuffle quer dizer embaralhar uma lista,valores,etc.... com a função random
 #random -> randomizador, números aleatórios entre 0 e 1
shuffle(lista) # Embralhara a ordem de nomes contidos na lista , apenas a ordem dos termos, criando uma "nova lista"
print('A ordem de apresentação será : {}{}{} '.format('\033[1;4;34m' , lista , '\033[m'))