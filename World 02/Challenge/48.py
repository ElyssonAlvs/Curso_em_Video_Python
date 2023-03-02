"""
Programa que calcule a soma entre todos os numeros impares que são múltiplos
de 3 entre 1 e 500

Program that calculates the sum of all odd numbers that are multiples of 3 
between 1 and 500
"""
total = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        total += i
print(total)
