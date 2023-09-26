"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez digitado pelo usuário.O programa será interrompido
quando o número solicitado for negativo.
"""
print("-----------------")
print("TABUADA INFINITA")
print("-----------------")
# Inicializamos um loop infinito usando 'while True'
while True:
    # Pedimos ao usuário para digitar um número e o convertemos para um inteiro
    numero = int(
        input(
            "Digite um número para ver a tabuada (digite um número negativo para sair): "
        )
    )

    # Verificamos se o número é negativo para encerrar o programa
    if numero < 0:
        print("Programa encerrado. Até a próxima!")
        # Usamos 'break' para sair do loop
        break

    # Se o número não for negativo, exibimos a tabuada para ele
    print(f"Tabuada do {numero}:")
    # Usamos um loop 'for' para iterar de 1 a 10
    for i in range(1, 11):
        # Calculamos o resultado multiplicando o número pelo índice do loop
        resultado = numero * i
        # Exibimos a equação e o resultado da multiplicação
        print(f"{numero} x {i} = {resultado}")
