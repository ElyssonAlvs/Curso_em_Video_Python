print('-' * 50 )
s = float(input('Qual o salário do funcionário ? '))
if s >= 1250 :
    novo  = s + (s * (10/100))
    print('Seu novo salário será de UR${} '.format(novo))
else :
    novo = s + (s * (15/100))
    print('Seu novo salário será de UR${} '.format(novo))
print('Quem ganhava R${:.2f}\npassa a ganhar R$ {:.2f} agora ' .format(s , novo))
print('-' * 50)