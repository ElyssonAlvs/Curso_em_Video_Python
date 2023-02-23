import random # Biblioteca utilizada , eles randomiza , embaralha uma lista ou numéros  , se for aplicada sozinha ela randomiza apenas números entre 0 e1
# Primeira forma de resolução :

print('\033[1;30m------------------------------------------------\033[m')
n = int(input('\033[4;33mEscolha um número entre 0 e 5 \033[m: ')) # Digite o número que você escolheu para sortear
l = [ 0, 1 , 2 , 3 , 4 , 5] # Lista na qual os números serão sortiados , como se fosse um local pra embaralhar os números
e = random.choice(l) # A função irá randomizar a lista indicada após o ponto , embaralhando a seguência de números nela
# Início da função condicional composta
if n == e :
    print('\033[4;34mVOCÊ ACERTOU !!!\033[m ') # SE , o número escolhido pelo usuário for igual ao resultado da randomização , ele acertou
else :
    print('\033[4;31mVOCÊ ERROU !!!!\033[m') # SE NÃO , o núemro escolhido for diferente do randomizado , o usuário errou
print('\033[1;30m-------------------------------------------------\033[m')

print('\033[1;30m-*-\033[m' * 50)

# Segunda forma de resolução :
# No caso seria uma brincadeira entre homem e máquina

computador = random.randint (0,5) # Faz o computador 'PENSAR' , usa a função random para randomizar e randint para ser entre um número e outro -> entre 0 e 5
print('\033[1;30m-=-\033[m' * 20)
print('\033[4;33mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m') # Usuário
print('\033[1;30m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei ? '))
if jogador == computador:
    print('\033[4;34mPARABÉNS!\033[m Você conseguiu me vencer ! ') # SE , o número do computador for igual ao do jogador , o jogador acertou
else:
    print('\033[4;31mGANHEI!\033[m Eu pensei o número \033[1;4;30m{}\033[m e não no \033[4;32m{}\033[m'.format(computador , jogador))
    # SE NÃO , o núemro de computador for diferente do jogador ,e o jogador errou