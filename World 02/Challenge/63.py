"""
Programa leia um número n inteiro qualquer e mostre os n primeiros elementos
de uma Sequência de Fibonacci
ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

Program reads any integer n and displays the first n elements
of a Fibonacci Sequence
ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
number = int(input('Write a number: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
couter = 3
while couter <= number:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    couter += 1
print(' -> Finish...')
