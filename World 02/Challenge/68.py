"""
Faça um programa que jogue par ou ímpar com o computador.
O programa só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
Digite um valor, Se par ou Ímpar o computador escolher um número, e a
soma dele vai determinar a vitória.
"""
from random import randint

print("-------------")
print("PAR ou ÍMPAR")
print("-------------")
import random  # Importa o módulo random para gerar números aleatórios

vitorias_consecutivas = 0  # Inicializa o contador de vitórias consecutivas

while True:
    jogador_escolha = input("Escolha par (P) ou ímpar (I): ").strip().upper()

    if jogador_escolha not in ("P", "I"):
        print("Escolha inválida. Digite 'P' para par ou 'I' para ímpar.")
        continue

    jogador_numero = int(input("Digite um número: "))
    computador_numero = random.randint(
        1, 10
    )  # O computador escolhe um número aleatório de 1 a 10
    soma = jogador_numero + computador_numero

    print(
        f"Você escolheu {jogador_numero} e o computador escolheu {computador_numero}."
    )
    print(f"A soma é {soma}.")

    # Verifica se a soma é par ou ímpar
    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    # Verifica se o jogador ganhou
    if resultado == jogador_escolha:
        print("Você ganhou!")
        vitorias_consecutivas += 1
        print(f"Vitórias consecutivas: {vitorias_consecutivas}")
    else:
        print("Você perdeu!")
        break  # Sai do loop se o jogador perder

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")
