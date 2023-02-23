print('----------------------------------------')
a = int(input('Qual o primeiro número ? '))
b  = int(input('Qual o segundo número ? '))
c = int(input('Qual o terceiro  número ? '))
# Verificando quem é menor
menor = a
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
print('O menor valor digitado foi {} '.format(menor))
print('O maior valor digitado foi {} '.format(maior))

