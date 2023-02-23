n = int(input('\033[4;30mDigite um número\033[m :')) # Digite o número
uni = n % 10
dez = n % 100
cent =n % 1000
mil =n % 10000
print('Unidade:\033[1;31m{}\033[m'.format(uni))
print('Dezena:\033[1;32m{}\033[m'.format(dez - uni))
print('Centena:\033[1;33m{}\033[m'.format(cent - dez))
print('Milhar:\033[1;34m{}\033[m'.format(mil - cent))

print("Outras 2 formas : ")
# Primeira forma
n = int(input("Irforme um número :  "))
n = str(n)
print("Analisando o número \033[1;4;30m{}\033[m".format(n))
print("Unidade : \033[1;31m{}\033[m".format(n[3]))
print("Dezena : \033[1;32m{}\033[m".format(n[2]))
print("Centena : \033[1;33m{}\033[m".format(n[1]))
print("Milhar :\033[1;34m{}\033[m".format(n[0]))
# Segunda forma
n = int(input("Irforme um número : "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("Analisando o número {}".format(n))
print("Unidade : \033[1;31m{}\033[m".format(u))
print("Dezena : \033[1;32m{}\033[m".format(d))
print("Centena : \033[1;33m{}\033[m".format(c))
print("Milhar : \033[1;34m{}\033[m".format(m))
