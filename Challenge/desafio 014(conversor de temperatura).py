C = float(input('\033[4;36mDiga a temperatura em °C\033[m :')) # Digite a temperatura em celsius para fazer a conversão
F = ((9*C)/5)+32 # Equação para converter Celsius em Fahrenheit
K = ((5*C)/5 )+ 273 # Equação para converter Celsius em Fahrenheit
print('A temperatura {}{}{}°C corresponde a {}{}{}°F\n'
      'e a {}{}{}K'.format('\033[4;32m' ,C ,'\033[m' , '\033[4;33m' , F ,'\033[m' ,'\033[4;35m' , K ,'\033[m'))
# No final seram apresentados o valor em Celsius convertido para Kelvin e Fahrenheit
