"""
Programa leia nome, idade, sexo de 4 pessoas e mostre:
    - Média da idade de todos
    - Nome do homem mais velho
    - Quantas mulheres tem menos de 20 anos

Program read name, age, gender of 4 people and show:
    - Average age of all
    - Oldest man's name
    - How many women are under 20 years old
"""
womam = 0
total_age = 0
counter = 0
older_man = 0
old_name = ''
total_woman_20 = 0
for i in range(1, 5):
    counter += 1
    print(f'-----{i}° People-----')
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    sex = str(input('Sexo [M/W]: ')).strip()
    total_age += age
    if i == 1 and sex in 'Mm':
        older_man = age
        old_name = name
    if sex in 'Mm' and age > older_man:
        older_man = age
        old_name = name
    if sex in 'Ww' and age < 20:
        total_woman_20 += 1
mean = total_age/4
print(f'Mean of ages: {mean}')
print(f'Older man: {old_name}, {older_man}')
print(f'Number of women under 20 : {total_woman_20}')
