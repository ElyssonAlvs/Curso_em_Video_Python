# Serviço de aluguel de carro
d = int(input('\033[1;31mPor quantos dias você usou o carro\033[m ?')) # Digite a quantidade de dias que usou o carro
km = float(input('\033[1;33mQuantos km você andou com ele \033[m?')) # Digite quantos kilômetro andou com carro
p1 = d*60 # Operação para converter os dias de uso do carro em valor a ser cobrado pelo serviço
p2 = km*0.15 # Operação para converter distância percorrida em valor a ser cobrado pelo serviço
t = p1 + p2 # Operação do total a ser pago pelo usuário do serviço
print('O total a pagar será \033[1;4;35mUR${}\033[m'.format(t))