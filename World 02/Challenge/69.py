"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, programa deverá perguntar se o
usuário quer ou não continuar.
No final, mostre:
    A) Quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.
"""
# Inicializa as variáveis para contar as estatísticas
pessoas_mais_de_18 = 0
homens_cadastrados = 0
mulheres_menos_de_20 = 0

while True:
    print("== Cadastro de Pessoa ==")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()

    # Verifica a idade e o sexo da pessoa
    if idade > 18:
        pessoas_mais_de_18 += 1
    if sexo == "M":
        homens_cadastrados += 1
    elif sexo == "F" and idade < 20:
        mulheres_menos_de_20 += 1

    continuar = (
        input("Deseja cadastrar outra pessoa? (S para Sim, N para Não): ")
        .strip()
        .upper()
    )

    if continuar != "S":
        break  # Sai do loop se o usuário não quiser continuar cadastrando

# Exibe as estatísticas no final
print(f"Total de pessoas com mais de 18 anos: {pessoas_mais_de_18}")
print(f"Total de homens cadastrados: {homens_cadastrados}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_de_20}")
