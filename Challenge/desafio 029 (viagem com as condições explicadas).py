# Primeira forma de resolução :
print('\033[1;4;30m------------------------------------------------------\033[m')
v = float(input('\033[4;30mQual a velocidade do carro (Km/h)\033[m ?')) # Informar qual a velocidade do carro no instante exato
vminimo = 80
# Início da condicionall composta :

if v <= vminimo :
    print('\033[4;32mVERDE\033[m') # SE , a velociade do carro for menor ou igual ao do limite , o sinal será verde
else :
    m =  (v - vminimo ) * 7
    # aplicando a equação -> a velocidade fornecida menos a velocide mínima vezes 7 ( o valor da multa pro quilômetro ultapassado)
    print('VOCÊ FOI \033[4;31mMULTADO\033[m E SUA MULTA FOI DE ' '\033[4;34m', m , '\033[m' 'R$')
    # SE NÃO , a velociade do carro excedeu o limite permitido
# Fim da Condicional composta
print('------------------------------------------------------')
# Segunda forma de resolução :
velocidade = float(input('\033[4;32mQual a velocidade atual do carro\033[m ? ')) # Informar a velocide do carro no momento
if velocidade > 80 :
    print('\033[4;31mMULTADO!\033[m Você excedeu o limite que é de \033[4;30m80 km/h\033[m ')
    # SE , a velociade do carro for maior que 80( miínima) , ele será multado
else :
    multa = (velocidade - 80 ) * 7 # Equação da multa seria a velociade do carro menos a mínima (80) vezes 7 ( o valor a ser pago pro cada quilômetro ultrapassdo)
    print('Você deve pagar uma multa de \033[4;31m{:.2f}\033[m ! '.format(multa))
    # SE NÃO , a velociade do carro for maior qua mínima permitida , a multa será aplicada , junto com um aviso de segurança
print('Tenha um \033[4;33mBom dia\033[m ! Dirija com segurança !')