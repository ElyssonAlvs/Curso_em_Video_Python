from random import choice # Biblioteca utilizada e a função utilizada
# Um apanhado de cores que será utilizado no código
cores = {'limpa': '\033[m',
       'azul': '\033[1;4;34m',
       'vermelho': '\033[1;4;31m',
       'verde': '\033[1;4;32m',
       'branco': '\033[4;30m'}
a1 = str(input('\033[4;35mNome do primeiro aluno\033[m : ')) # Digite o nome do primeiro aluno
a2 = str(input('\033[4;37mNome do segundo aluno\033[m : ')) # Digite o nome do segundo aluno
a3 = str(input('\033[4;30mNome do terceiro aluno\033[m : ')) # Digite o nome do terceiro aluno
a4 = str(input('\033[4;36mNome do quarto aluno\033[m : ')) # Digite o nome do quarto
lista = [a1 , a2 , a3 , a4 ] # Lista do aluno digitados
escolhido = choice(lista) # Embaralhamento da lista para realizar uma escolha aleatória
# Início da Estrutura Condicional Simples
if escolhido == a1 :
    print('O aluno escolhido foi o {}{}{}'.format(cores['azul'] , a1 , cores['limpa']))
if escolhido == a2 :
    print('O aluno escolhido foi o {}{}{}'.format(cores['vermelho'] , a2 , cores['limpa']))
if escolhido == a3 :
    print('O aluno escolhido foi o {}{}{}'.format(cores['verde'] , a3 , cores['limpa']))
if escolhido == a4 :
    print('O aluno escolhido foi o {}{}{}'.format(cores['branco'] , a4 , cores['limpa']))
# Fim da Estrutura Condiconal Simples