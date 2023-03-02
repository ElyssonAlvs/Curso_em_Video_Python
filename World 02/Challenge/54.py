"""
Programa que leia o ano de nascimento de sete pessoas, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são de maior
Maioridade -> 21 anos
"""
from datetime import date
today = date.today().year
age_of_majority = 0
not_age_of_majority = 0
for i in range(1, 8):
    year = int(input('Write a bith year: '))
    m = today - year
    if m >= 21:
        age_of_majority += 1
    elif m < 21:
        not_age_of_majority += 1
print(f'Numbers of older people: {age_of_majority}')
print(f'Numbers of minors: {not_age_of_majority}')
