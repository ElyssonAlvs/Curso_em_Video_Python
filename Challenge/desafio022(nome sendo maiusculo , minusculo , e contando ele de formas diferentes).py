from time import sleep
nome = str(input('\033[4;34mQual o seu nome\033[m?')).strip() # Digite o nome , strip irá retirar os espaços que ficam sobrando na esquerda e direita
print('Analisando seu nome...') # Analisando o nome listado
sleep(2)
print('Seu nome em maiúsculas é \033[4;34m{}\033[m'.format(nome.upper())) # Colocará o nome listado para maiúsculo
print('Seu nome em minúsculas é \033[1;34m{}\033[m'.format(nome.lower())) # Colocará o nome listado para minúsculo
print('Seu nome têm ao todo \033[1;4;34m{}\033[m letras'.format(len(nome) - nome.count(' '))) # Irá contar a quantidade de letras do nome , mas com a função count irá retirar os espaços entre o nome
# print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() # Separa o nome em listas
"""EX
nome = Roberto Carlos -> nome = ['Roberto', 'Carlos']
"""
print('Seu primeiro nome é \033[1;4;31m{}\033[m e ele têm \033[1;4;33m{}\033[m letras'.format(separa[0], len(separa[0])))
# Como o primeiro nome é aquele que for listado ele terá com indentifição 0 e assim com a função len , mostrará quantas letras esse componente tem