"""
Programa que leia o ano de nascimento de um atleta e mostra sua categoria, de acordo
com a idade:
- até 9 anos : Mirim
- até 14 anos : Infantil
- até 19 anos : Junior
- até 25 anos : Sênior
- Acima : Master

Program that reads the year of birth of an athlete and shows his category, according to
With the age:
- up to 9 years: Mirim
- up to 14 years: Infant
- up to 19 years: Junior
- up to 25 years: Senior
- Above: Master
"""
from datetime import date
birth_year = int(input('Bith Year:'))
category = date.today().year - birth_year
if category <= 9:
    print('MIRIM')
elif category <= 14:
    print('INFANT')
elif category <= 19:
    print('JUNIOR')
elif category >= 20:
    print('SENIOR')
else:
    print('MASTER')
