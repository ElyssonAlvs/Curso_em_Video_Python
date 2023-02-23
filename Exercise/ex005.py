#nome=str(input('Qual o seu nome ?'))
#print('prazer em te conhecer {:=^20}!'.format(nome))
#print('iai {:<10}!'.format(nome))
#print('iai {:>10}!'.format(nome))
#print('iai {:10}!'.format(nome))
n1=int(input('digite um valor :'))
n2=int(input('digite outro valor:'))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
di = n1 // n2
p = n1**n2
m = n1 * n2
#print('a soma vale {} ,a subtração vale {} e a divisão vale {} '.format( s, sub, d))
#print('a soma vale {} ,a subtração vale {} e a divisão vale {:.3f} '.format( s, sub, d))
print('a soma vale {} ,a subtração vale {} e a divisão vale {:.3f} '.format( s, sub, d),end=' ')
print('e a divisão inteira equivale a {} a potência {} enquanto a multiplição {}'.format( di, p, m))