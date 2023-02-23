from time import sleep
cidade = str(input("\033[4;31mDigite o nome de uma cidade\033[m : ")).strip() # Digite o nome da cidade que será analisada (a função irá retirar os espaços inúteis nas extremidades)
print("\033[1;4;30mAnalisando a cidade informada\033[m...") # Decoração
sleep(1)
print(cidade[:5].upper() == "SANTO") # A cidade analisada , se começar com "SANTO" retornará 'true' se não 'false'