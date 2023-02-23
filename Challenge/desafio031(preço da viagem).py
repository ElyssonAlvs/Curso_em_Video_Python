print('---------------------------------------------------------')
d = float(input('Qual a distância que você irá percorrer (Km) ? '))
if d <= 200 :
    v =  d * 0.5
    print('VOCÊ PAGARÁ PELA VIAGEM R$ ' , v )
else :
    v = d * 0.45
    print('SUA VIAGEM FOI LONGA PORTANTO VOCÊ PAGARÁ R$' ,  v )
print('----------------------------------------------------------')

print('-§-' * 50 )

distância = float(input('Qual é a distância da sua viagem ? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
if distância <= 200 :
    preço = distância * 0.50
else :
    preço = distância * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))

print('-§-' * 50)

distância = float(input('Qual é a distância da sua viagem ? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))