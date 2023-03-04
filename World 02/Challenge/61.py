"""
Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 
primeiro termos da prograssão usando a estrutura while
"""
first_term = int(input('Write a first term of PA: '))
r = int(input('Write a reason of PA: '))
ten_term = first_term + (10 - 1) * r
while first_term < ten_term + r:
    print(first_term, end=' -> ')
    first_term += r
print('End!')
