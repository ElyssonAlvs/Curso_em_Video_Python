# Estruturas de controle - while
# Exemplo 1
cont = 1
while cont <= 10:
    print(cont, "-> ", end="")
    cont += 1
print("Acabou")
# Exemplo 2
numero = soma = 0
while True:
    numero = float(input("Digite um número: "))
    if numero == 999:
        break
    soma += numero
print(f"A soma vale {soma:.2f}")
