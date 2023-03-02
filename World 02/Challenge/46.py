"""
Programa que mostra uma contagem regreessiva
para o estouro de fogos de artifício, indo de 
10 até 0, com uma pausa de 1 segundo entre eles

Program that displays a countdown
for the burst of fireworks, going from
10 to 0, with a 1 second pause between them
"""
from time import sleep
print('Fireworks will start in 10 seconds:')
for i in range(10, -1, -1):
    print(i)
    sleep(0.5)
print('Released!')
