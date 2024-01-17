"""
Crie um programa que simule o funcionamento de uma caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(int)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que a caixa possui cédulas de 50,20,10 e 5
"""
# Solicita o valor a ser sacado ao usuário
valor_saque = int(input("Digite o valor a ser sacado: R$"))

# Inicializa as variáveis para contar as cédulas
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_5 = cedulas_1 = 0

# Calcula as cédulas
while valor_saque > 0:
    if valor_saque >= 50:
        cedulas_50 += 1  # Incrementa a quantidade de cédulas de R$50
        valor_saque -= 50  # Subtrai R$50 do valor total
    elif valor_saque >= 20:
        cedulas_20 += 1  # Incrementa a quantidade de cédulas de R$20
        valor_saque -= 20  # Subtrai R$20 do valor total
    elif valor_saque >= 10:
        cedulas_10 += 1  # Incrementa a quantidade de cédulas de R$10
        valor_saque -= 10  # Subtrai R$10 do valor total
    elif valor_saque >= 5:
        cedulas_5 += 1  # Incrementa a quantidade de cédulas de R$5
        valor_saque -= 5  # Subtrai R$5 do valor total
    elif valor_saque >= 1:
        cedulas_1 += 1
        valor_saque -= 1
    else:
        print("Não é possível sacar o valor solicitado com as cédulas disponíveis.")
        break  # Sai do loop se não for possível fazer o saque com as cédulas disponíveis

# Exibe as cédulas a serem entregues
if cedulas_50 > 0:
    print(f"Cédulas de R$50: {cedulas_50}")
if cedulas_20 > 0:
    print(f"Cédulas de R$20: {cedulas_20}")
if cedulas_10 > 0:
    print(f"Cédulas de R$10: {cedulas_10}")
if cedulas_5 > 0:
    print(f"Cédulas de R$5: {cedulas_5}")
if cedulas_1 > 0:
    print(f"Cédulas de R$1: {cedulas_1}")
