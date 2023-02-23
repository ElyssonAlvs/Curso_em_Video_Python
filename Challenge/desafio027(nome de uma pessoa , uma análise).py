n = str(input('\033[4;30mDigite seu nome completo\033[m : ')).strip() # Digite o seu nome , com a função strip() ele irá retirar os espaços em branco
nome = n.split() # A função irá pegar o nome e colocará cada palavra em um lista (uma separada de outra)
print('Muito prazer em te conhecer\033[m') # Decoração
print('O seu primeiro nome é \033[4;31m{}\033[m'.format(nome[0])) # Nesse caso seria o número "0" da lista criada pela função n.split
print('O seu último nome é \033[4;34m{}\033[m'.format(nome[len(nome)-1]))
# Ele vai pegar a lista do nome , realizar o len(contar quantas palavras tem na strig) ,
# Na contagem da lista(0,1,2,3...) tem-se uma contagem , na do len tem outra mas a
# contagem(1,2,3...) do len vai ser maior portanto , para "igualar" os números diminui -1 .

