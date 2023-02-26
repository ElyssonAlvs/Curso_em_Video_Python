"""
Programa que leia um número inteiro e peça para o usuário escolher
qual será a base de conversão:
1 - binário
2 - octal
3 - hexadecimal

Program that reads an integer and asks the user to choose
what will be the base conversion:
1 - binary
2 - octal
3 - hexadecimal
"""
number = int(input('Write a number:'))
print('''What base do you want to converto this number?
1 - binary
2 - octal
3 - hexadecimal''')
op = int(input('You option : '))
if op == 1:
    print(f'Number in binary base: {bin(number)[2:]}')
elif op == 2:
    print(f'Number in octal base: {oct(number)[2:]}')
elif op == 3:
    print(f'Number in hexadecimal base: {hex(number)[2:]}')
else:
    print('No options, try again.')
