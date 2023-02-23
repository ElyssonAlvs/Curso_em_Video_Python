nome = str(input("\033[1;34mDigite seu nome completo\033[m : ")).strip() # Digite o nome que será analisado (a função irá retirar os espaços inúteis nas extremidades)
verificador = "SILVA" in nome.upper() # Ele irá procurar a palavra 'SILVA' no nome em *maiúsculo*
print("Seu nome tem Silva ? \033[1;4;30m{}\033[m".format(verificador))