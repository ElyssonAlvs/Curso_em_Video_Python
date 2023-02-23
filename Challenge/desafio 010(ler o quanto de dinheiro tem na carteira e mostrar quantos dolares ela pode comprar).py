r = float(input('\033[4;32mMeu amigo,quantos reais você têm na sua carteira \033[m? R$')) # Digite quanto seu amigo tem na carteira
dolar = r/5.46 # Operação para converter reias em dólar
euro = r/4.66 # Operação para converter reais em euro
libra = r/5.44 # Operação para converter reais em libra esterlina
print('Com \033[4;32mUR${:.2f}\033[m você pode comprar \033[4;31mU${:.2f} dólares\033[m\n'
      'Com \033[4;32mUR${:.2f}\033[m você pode comprar \033[4;30m¢{:.2f} euros\033[m\n'
      'Com \033[4;32mUR${:.2f}\033[m você pode comprar \033[4;34m£{:.2f} libras esterlinas\033[m'.format(r, dolar, r, euro, r, libra ))
#Conversao de valores se pega o valor que se quer converter e dividi pelo valor que se apresenta ex:1 real = 4.70