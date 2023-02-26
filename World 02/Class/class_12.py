name = str(input('What is your name ?'))
if name == 'Elysson':
    print('This is a beautiful name')
elif name == 'Peter' or name == 'Maria' or name == 'Paul':
    print('Your name is very famous in Brasil.')
elif name in 'Ana Elizabeth Rose Julie':
    print('This is beautiful female name')

print(f'Good Morning, {name}')