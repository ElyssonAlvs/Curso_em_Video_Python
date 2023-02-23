from time import sleep

print('\033[1;34mOlá mundo!')
sleep(1)
print('\033[1;31;43mOlá mundo!\033[m')
sleep(1)
print('\033[4;30;45mOlá mundo!\033[m')
sleep(1)
print('\033[7;30mOlá mundo!\033[m')
sleep(1)
print('\033[0;33;44mOlá mundo!\033[m')
sleep(1)
print('\033[7;33;44mOlá mundo!\033[m')
sleep(2)
a = 3
b = 5
print('Oa valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a , b ))
print('Oa valores são \033[4;32m{}\033[m e \033[4;31m{}\033[m!!!'.format(a , b ))
sleep(3)
nome = 'Elysson'
print('Muito prazer em te conhecer , {}{}{} !!!'.format('\033[4;31m' , nome , '\033[m'))
sleep(3)
nome = 'Elysson'
cores = {'limpa' : '\033[m' ,
         'azul' :'\033[34m' ,
         'amarelo' : '\033[33m' ,
         'pretoebranco' : '\033[7;30m'}
print('Muito prazer em te conhecer , {}{}{} !!!'.format( cores ['azul'] , nome , cores['limpa']))