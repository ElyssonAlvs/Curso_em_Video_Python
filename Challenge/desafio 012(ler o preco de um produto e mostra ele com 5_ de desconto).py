preco = float(input('\033[4;30mO preço do produto é de ?\033[m')) # Digite o preço do produto
des = preco - (preco * (5/100)) # Operação para dar desconto ao preço do produto
#print('Mas como estamos em oferta o produto recebeu um 5% de\n'
     # 'desconto,ficando por apenas {:.2f} !'.format(des))
aum = preco + (preco * (8/100)) # Operação para dar o aumento de preço do produto
print('Mas dependendo de como o senhor quiser comprar o produto temos ele \n'
      'a vista com 5% de desconto ficando por \033[4;32mUR${}\033[m,mas se você quiser parcelar\n'
      'em até 8x o preço terá um aumento de 8% ficando por \033[4;31mUR${}\033[m.'.format(des, aum))