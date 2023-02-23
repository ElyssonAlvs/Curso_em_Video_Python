# Forma de fazer ¹
'''import math
num = float(input('Digite um número:'))
pI = math.trunc(num)
# 'Truncar' um número significa pegar apenas a sua parte inteira
print('O número {} tem perte intera igual a {}'.format(num, pI))'''
# Forma de fazer ²
num = float(input('\033[1;33mDigite um valor\033[m :')) # Digite um valor para mostrar a sua parte inteira
print('O valor digitado foi \033[1;33m{}\033[m e sua porção inteira é \033[1;34m{}\033[m .'.format(num, int(num)))
# posso pegar um float e transforma-lo em int, redefinindo seu tipo dentro da formatação