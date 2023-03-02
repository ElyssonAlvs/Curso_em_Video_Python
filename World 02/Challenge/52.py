"""
Programa que leia um número e mostre se ele é primo ou não

Program that reads a number and shows if it is prime or not
"""
total = 0
number = int(input('Write a number: '))
for i in range(1, number + 1):
    if number % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print(f'{i}', end=' ')
if total == 2:
    print('\nIs prime')
else:
    print('\nIs not prime')
