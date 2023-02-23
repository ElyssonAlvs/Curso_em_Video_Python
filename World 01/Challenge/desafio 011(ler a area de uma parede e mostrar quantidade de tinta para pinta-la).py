alt =float(input('\033[4;31mQual a altura da parede que será pintada \033[m? ')) # Digite a altura da parede que será pintada
lar = float(input('\033[4;34mQual a sua largura\033[m?')) # Digite a largura da parede
area = alt * lar # Operação para calcullar a área da parede que será pintada
tinta = area/2 # Operação para calcular a quantidade de tinta que será utilizada para pintar a parede
print('As dimensões da sua parede sao \033[1;34m{}\033[mx\033[1;31m{}\033[m sendo assim a sua área é \033[1;33m{:.2f}m²\033[m,\n'
      'consequentemente quantidade de litros de tinta que será usada para\n'
      'pintá-la será de \033[1;30m{:.2f}L\033[m'.format(alt, lar, area, tinta))