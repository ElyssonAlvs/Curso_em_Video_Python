m =float(input('\033[1;4;30mO valor da  medida em metros \033[m:')) # Digite o valor da medida em metros que deseja converter
km = m/1000 # Operação para converter metros em quilômetros
hm = m/100 # Operação para converter metros em hectômetros
dam = m/10 # Operação para converter metros em decâmetros
dm = m*10 # Operação para converter metros em decímetros
c = m*100 # Operação para converter metros em centímetros
mm = m*1000 # Operação para converter metros em milímetros
print("""A medida \033[1;4;31m{}m\033[m \nem milímetros vale \033[1;4;32m{}mm\033[m\ncentímetros vale \033[1;4;33m{}cm\033[m
decímetros vale \033[1;4;34m{}dm\033[m \nem decâmetros \033[1;4;35m{}dam\033[m \nhectômetros vale \033[1;4;36m{}hm\033[m 
e em quilômetros \033[1;4;37m{}km\033[m . """.format(m, mm, c, dm, dam, hm, km))




