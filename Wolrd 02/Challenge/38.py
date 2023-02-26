"""
Programa que leia dois números inteiros e compare-os mostrando na tela
uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais

Program that reads two integers and compares them showing on the screen
a message:
- The first value is greater
- The second value is greater
- There is no greater value, both are equal
"""
number1 = int(input('Write a first number:'))
number2 = int(input('Write a second number:'))
if number1 > number2:
    print('The first number is greater.')
elif number2 > number1:
    print('The second number is greater')
elif number1 == number2:
    print('There is no greater number, the numbers are equal.')
