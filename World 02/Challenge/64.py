"""
Programa leia vários inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final
mostre quantos números foram digitados e qual foi a soma entre eles.

Program reads several integers from the keyboard. The program will only stop when the user
types the value 999, which is the stop condition. At the end, show how many numbers were 
entered and what was the sum between them.
"""
number = int(input('Write a number: '))
counter = 0
total = 0
while number != 999:
    counter += 1
    total += number
    number = int(input('Write a number: '))
print(counter)
print(total)
