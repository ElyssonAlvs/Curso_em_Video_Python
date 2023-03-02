"""
Programa leia seis números e mostre a soma dos pares, se o número
digitado for ímpar, desconsiderar

Program reads six numbers and prints the sum of the pairs, if the number
entered is odd, disregard.
"""
total = 0
for i in range(1, 7):
    number = int(input('Write a number: '))
    if number % 2 == 0:
        total += number
    else:
        pass
print(total)
print('The end')
