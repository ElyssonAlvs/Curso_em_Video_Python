"""
Programa leia vários números inteiros pelo teclado No final mostre a média
entre todos os valores e qual foi o maior e o menor valor lido. O programa
deve perguntar se o usuário quer ou não continuar a digitar valores

Program reads several integers through the keyboard At the end it shows the average 
between all values ​​and which was the highest and lowest value read. The program should
ask whether or not the user wants to continue typing values
"""
resp = 'S'
soma = quant = m = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Continuar? [S/N] -> ')).upper().strip()[0]
m = soma/quant
print('Média: {:.2f}', format(m))
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print('Acabou')
