import random # Bibllioteca que será utilizada
"""
a = random.randint(1,4) vai sortear um número entre 1 e 4, dentre desse intervalo
print('O aluno escolhido foi o aluno de número.......{}!'.format(a)) -> primeira vez sortiando com números aletórios""" 
a1 = input('\033[4;34mNome do primeiro aluno\033[m :') # Digite o nome do primeiro aluno
a2= input('\033[4;31mNome do segundo aluno\033[m :') # Digite o nome do segundo aluno
a3= input('\033[4;33mNome do terceiro aluno\033[m :') # Digite o nome do terceiro aluno
a4 = input('\033[4;32mNome do quarto aluno\033[m :') # Digite o nome do quarto aluno
lista =  [a1, a2, a3, a4] # Lista que contém os nomes dos alunos listados
escolhido = random.choice(lista) # Função para realizar uma escolha dentre as disponíveis na lista
print('O aluno escolhido foi \033[1;4;30m{}\033[m'.format(escolhido)) # Mostrará o nome do aluno sortiado
#choice é escolher um valor das respostas do input,coloca-se a lista com colchetes determina a variável com o comando random.choice(lista das informções)