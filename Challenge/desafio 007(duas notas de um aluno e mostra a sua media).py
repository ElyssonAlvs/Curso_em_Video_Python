nota01 =float(input('\033[1;34mA primeira nota do aluno  \033[m :')) # Digite o número para reallizar sua média ¹
nota02 =float(input('\033[1;31mA segunda nota do aluno  \033[m :')) # Digite o número para realizar a média ²
m = (nota01+nota02)/2 # Equação para realizar a média dos número informados
print('Por fim a sua média nas duas avaliações foi {}{:.1f}{} '.format('\033[4;33m', m , '\033[m' )) # Resultado da média dos números apresentados