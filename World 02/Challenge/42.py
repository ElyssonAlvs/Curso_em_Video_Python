"""
Desafio 35 (Mundo 01), dos triângulos, acrescentando a recurso de mostrar que tipo
de triângulo será formado:
- Equilátero : todos os lados iguais
- Isósceles : dois lados iguais
- Escaleno : todos os lados diferentes

Challenge 35 (World 01), of the triangles, adding the feature of showing what type
of triangle will be formed:
- Equilateral: all sides equal
- Isosceles: two equal sides
- Scalene : all different sides
"""
print('-=' * 20)
print('Analyzing the triangle')
print('-=' * 20)
r1 = float(input('First side:'))
r2 = float(input('Second side:'))
r3 = float(input('Third side:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('The given sides can form a triangle.')
    if r1 == r2 == r3:
        print('An equilateral triangle.')
    elif r1 != r2 != r3 != r1:
        print('An scalene triangle.')
    else:
        print('An isósceles triangle.')
else:
    print('The given sides can not form a triangle.')
