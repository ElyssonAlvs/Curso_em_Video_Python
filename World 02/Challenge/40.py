"""
Programa que leia duas notas de uma aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média:
- Média abaixo de 5.0 : Reprovado
- Média entre 5.0 e 6.9 : Recuperação
- Média 7.0 o superior: Aprovado

Program that reads two grades of a student and calculates their average, showing
a message at the end, according to the average:
- Average below 5.0: Failed
- Average between 5.0 and 6.9: Recovery
- Average 7.0 or higher: Approved
"""
note_01 = float(input('First note:'))
note_02 = float(input('Second note:'))
mean = (note_01 + note_02)/2
if mean < 5.0:
    print('FAILED 😥')
elif 7 > mean >= 5.0:
    print('RECOVERY 😑')
elif mean >= 7.0:
    print('APPROVED 😀')
