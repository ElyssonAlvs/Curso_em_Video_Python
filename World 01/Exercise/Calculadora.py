primeiroValor = float(input("Digite o primeiro número : "))
segundoValor = float(input("Digite o segundo número : "))
print(("Qual operação você deseja fazer ?"))
operacao = float(input("1 para soma , 2 para multiplicação, 3 para a subtração e 4 para divisão -> "))
if operacao == 1:
    resultado = primeiroValor + segundoValor
    print(f"{primeiroValor} + {segundoValor} = {resultado} ")
elif operacao == 2 :
    resultado = primeiroValor * segundoValor
    print(f"{primeiroValor} x {segundoValor} = {resultado} ")
elif operacao == 3 :
    resultado = primeiroValor - segundoValor
    print(f"{primeiroValor} - {segundoValor} = {resultado} ")
elif operacao == 4 :
    resultado = primeiroValor / segundoValor
    print(f"{primeiroValor} / {segundoValor} = {resultado:.2f} ")
else :
    print("Não sei fazer essa operação :(")