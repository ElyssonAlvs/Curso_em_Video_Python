"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$1000,00.
    C) Qual o nome do produto mais barato.
"""
# Inicializa as variáveis para as estatísticas
total_gasto = 0
produtos_mais_de_1000 = 0
produto_mais_barato_preco = contador = 0
barato = ''

while True:
    print("== CADASTRO PRODUTOS ==")
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))
    contador += 1

    # Atualiza o total gasto
    total_gasto += preco_produto

    # Verifica se o produto custa mais de R$1000
    if preco_produto > 1000:
        produtos_mais_de_1000 += 1

    # Verifica se este é o produto mais barato até agora
    if contador == 1 or preco_produto < produto_mais_barato_preco:
        produto_mais_barato_preco = preco_produto
        barato = nome_produto

    continuar = (
        input("Deseja cadastrar outro produto? (S para Sim, N para Não): ")
        .strip()
        .upper()
    )

    if continuar != "S":
        break  # Sai do loop se o usuário não quiser continuar cadastrando

# Exibe as estatísticas no final
print(f"Total gasto na compra: R${total_gasto:.2f}")
print(f"Quantidade de produtos com preço superior a R$1000,00: {produtos_mais_de_1000}")
print(f"O produto mais barato foi {barato} que custa {produto_mais_barato_preco:.2f}")
