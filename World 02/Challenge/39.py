"""
Programa que leia o ano de nascimento de um jovem e informe, de acordo com sua 
idade:
- Se ele ainda vai se alistar ao serviço
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

-> Deve mostrar o tempo que falta ou que passou do prazo

Program that reads the year of birth of a young person and informs, according to his
age:
- If he is still going to enlist in the service
- If it's time to enlist
- If it's past the enlistment time

-> It should show the time left or past the deadline
"""
from datetime import date
YEAR = date.today().year
year_of_birth = int(input('Year of Bith:'))
age = YEAR - year_of_birth
print(f'Who was born in the year {year_of_birth} is {age} years old in {YEAR}')
if age == 18:
    print('You must enlist NOW!')
elif age < 18:
    enlistment = 18 - age
    print(f'There are still {enlistment} years left for your enlistment')
    year_enlistment = YEAR + enlistment
    print(f'You enlistment will be in {year_enlistment} years')
elif age > 18:
    enlistment = age - 18
    print(f'You should have enlisted {enlistment} years ago')
    year_enlistment = YEAR - enlistment
    print(f'You enlistment is {year_enlistment}')
