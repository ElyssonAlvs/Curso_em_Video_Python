nome = str(input('\033[4;34mQual o seu nome\033[m ?')) # Digite um nome para registrar o input (strig)
# Início da Estrutura Condicional Composta
if nome == 'Elysson' :
    print('Que nome \033[4;31mlindo\033[m você tem!')
    # Se a resposta for "Elysson" ele mostrará o print
else :
    print('Seu nome é tão \033[37mnormal\033[m.')
    # Senão , ele mostrará outro print
# Fim da Estrutura Condicional Composta
print('\033[4;33mBom dia\033[m , {}!'.format(nome))
# Depedendo do input a Estrutura Condicional vai analisar e colocar a resposta que se encaixa nas condições exigidas
