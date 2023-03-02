"""
Tabuada do desafio 09, mostrando a tabuada de um número usando laço de repetição

Table of challenge 09, showing the table of a number using repeating loop
"""
number = int(input(('Write a number: ')))
for i in range(1, 11):
    print(f'{number} x {i} = {i*number}')
print('The end.')
