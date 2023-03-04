"""
Desafio 061 pergunta ao usuário se ele que mostrar alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos

Challenge 061 asks the user if he wants to show some terms.
The program exits when it says it wants to show 0 terms
"""
first_term = int(input('Write a first term: '))
r = int(input('What a reason of PA: '))
term = first_term
couter = 0
total = 0
m = 10
while m != 0:
    total += m
    while couter <= total:
        print(f'{term}', end=' -> ')
        term += r
        couter += 1
    print('Stop.')
    m = int(input('More numbers?: '))
print(f'{total} terms to PA')
