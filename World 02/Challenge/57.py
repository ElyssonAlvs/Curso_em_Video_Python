"""
Leia o sexo de uma pessoa, mas aceite apenas valores 'M' ou 'F'.
Caso esteja errado, tentar novamente até ter uma valor correto.

Read a person's gender, but accept only 'M' or 'F' values.
If it is wrong, try again until you have a correct value.
"""
s = str(input('Write a sex:'))
v = False
while v == False:
    s = str(input('Write a sex:'))
    if s == 'W' or s == 'M' or s == 'w' or s == 'm':
        v = True
print('The end.')
