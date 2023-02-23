# Importando a Biblioteca que será utilizada
import math 
print('-'*67) # Decoração, ficar mais legal de se ver
co = float(input('\033[4;30mTem-se um triângulo retângulo, qual o valor do seu cateto oposto\033[m?')) # Digite o valor do cateto oposto do triângulo retângulo
ca = float(input('\033[4;37mQual o valor de seu cateto adjacente\033[m?')) # Digite o valor do cateto adjacente do triângulo retângulo
hip = math.sqrt(pow(co, 2) + pow(ca, 2)) # Equação usada para calcular a hipotenusa (sqrt -> tirar a raiz quadrada do número)
print('Sendo o cateto oposto igual a \033[4;30m{}\033[m e o cateto adjacente igual a \033[4;37m{}\033[m\n' 
      'a hipotenusa será \033[4;31m{:.2f}\033[m . '.format(co, ca, hip))
# Utiliza-se a funçao format , a :.2f (para representa um número apenas com 2 dígito após a vírgula)
print('-'*67) # Decoração
#hip = hypot(co,ca) calcular a hipotenusa (por outro modo)