"""
Desafio 28 (mundo 01) + números de tentativas para acertar

Challenge 28 (World 01) + number of attempts to hit
"""
from random import randint
counter = 0
computer = randint(0, 10)
player = int(input('Write a number: '))
print('Again')
while computer != player:
    player = int(input('Write a number: '))
    counter += 1
    if computer == player:
        print('Hit!')
    else:
        print('Again')
print(f'Number of attempts to hit: {counter}')
