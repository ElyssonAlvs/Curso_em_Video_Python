"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

Create a program that reads two values ​​and displays a menu on the screen:

[ 1 ] add
[ 2 ] multiply
[3] bigger
[ 4 ] new numbers
[ 5 ] Exit the program

Your program should perform the requested operation in each case.
"""
n1 = int(input('Write a first number: '))
n2 = int(input('Write a second number: '))
option = 0
while option != 5:
    print('''Choice the option:
    [1] sum
    [2] mul
    [3] higher
    [4] new numbers
    [5] end program''')
    option = int(input('Option: '))
    if option == 1:
        sum = n1 + n2
        print(f'Sum: {sum}')
    elif option == 2:
        mul = n1 * n2
        print(f'Mul: {mul}')
    elif option == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Higher number: {maior}')
    elif option == 4:
        print('New number:')
        n1 = int(input('Write a first number: '))
        n2 = int(input('Write a second number: '))
    elif option == 5:
        print('Finish...')
    else:
        print('Again')
    
