"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor 999, que
é a condição de parada. No final mostra quantos números foram digitados
e qual foi a soma entre eles (desconsiderando a flag)
"""
numero = soma = contador = 0
while True:
    numero = int(input("Digite um número ou  999 para parar : "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(
    f"Quantidade de números digitados : {contador} "
    "\n"
    f"Soma dos números menos 999 : {soma}"
)
