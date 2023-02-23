salario = float(input('\033[4;30mQual o salario do funcionário ?\033[m')) # Digite o salário do funcinário
n = salario + (salario * (15/100)) # Operação para calcular o aumento do salário do funcionário
print('Mas a partir do próximo mês ele recberá um aumento de\n'
      '15% e irá receber \033[4;32mUR${}\033[m em seu novo cargo'.format(n))