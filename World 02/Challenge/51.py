"""
Programa leia o primeiro termo e a razão de uma PA, no final mostrar os 
10 primeiros termos
"""
first_term = int(input('Write a first term of PA: '))
r = int(input('Writa a reason of PA: '))
ten_term = first_term + (10 - 1) * r
for i in range(first_term, ten_term + r, r):
    print(i, end=' -> ')
print('End!')
