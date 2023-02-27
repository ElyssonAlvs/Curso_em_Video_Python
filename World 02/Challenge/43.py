"""
Programa que leia peso e a altura de uma pessoa e calcule o IMC de mostre seu status:
- 18.5 : Abaixo do peso
- 18.5 até 25 : Peso ideal
- 25 até 30 : Sobrepeso
- 30 até 40 : Obesidade
- Acima de 40: Obesidade mórbida

Program that reads a person's weight and height and calculates BMI and displays their status:
- 18.5 : Underweight
- 18.5 to 25 : Ideal weight
- 25 to 30 : Overweight
- 30 to 40 : Obesity
- Over 40: Morbid obesity
"""
from math import pow
weight = float(input('Write the weight(kg):'))
height = float(input('Write the height(m):'))
imc = weight / (pow(height, 2))
if imc < 18.5:
    print('UNDERWEIGHT')
elif 18.5 <= imc < 25:
    print('IDEAL WEIGHT')
elif 25 <= imc < 30:
    print('ABOVE')
elif 30 <= imc < 40:
    print('OBESITY')
elif imc >= 40:
    print('MORBID OBESITY')
