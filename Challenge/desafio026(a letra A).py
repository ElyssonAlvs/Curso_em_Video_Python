# Digite a frase que será analisada(a função strip retirará os espaços inúteis e em seguida colocará em maiúscula)
frase = str(input('Digite uma frase : ')).strip().upper()
# A Função mostrará quantas vezes a letra exigida aparece na string
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
# A Função 'encontrará' a letra A na sua primeira posição que para o computador a contagem começa no 0 , por isso adiciona +1 para ser compreendido por um humano
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
# A Função 'encontrará' a letra A na sua última posiçao(rfind irá começar pela 'right' direita para facilitar a busca) que para o computador a contagem começa no 0 , por isso adiciona +1 para ser compreendido por um humano)
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
