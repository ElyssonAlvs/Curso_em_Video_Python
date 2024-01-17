
---

# Estrutura de Repetição `while` com `break` em Python

Em Python, a estrutura de repetição `while` é utilizada para executar um conjunto de instruções repetidamente enquanto uma determinada condição for verdadeira. A declaração `break` é usada para interromper a execução do loop quando uma condição específica for atendida. Vamos analisar dois exemplos que demonstram a utilização do `while` com `break`.

## Exemplo 1: Contagem até 10

```python
cont = 1
while cont <= 10:
    print(cont, "-> ", end="")
    cont += 1
print("Acabou")
```

Neste exemplo, temos uma variável `cont` inicializada com o valor 1. O loop `while` é executado enquanto `cont` for menor ou igual a 10. A cada iteração, o valor de `cont` é impresso com a formatação "-> " e incrementado em 1. O loop continuará até que `cont` seja maior que 10, momento em que a condição do `while` não será mais atendida, e o loop será interrompido com a instrução `break`. A saída do programa será:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> Acabou
```

## Exemplo 2: Soma de Números

```python
numero = soma = 0
while True:
    numero = float(input("Digite um número: "))
    if numero == 999:
        break
    soma += numero
print(f"A soma vale {soma:.2f}")
```

Neste segundo exemplo, o loop `while` é criado com `while True`, o que significa que ele será executado indefinidamente até que seja interrompido pelo `break`. O programa solicita que o usuário insira números, e esses números são somados à variável `soma`. O loop continuará a receber números até que o usuário insira o valor 999, momento em que a condição `if numero == 999` será verdadeira, e o `break` interromperá o loop. Após a interrupção do loop, o programa imprimirá a soma dos números inseridos com duas casas decimais.

É importante usar o `break` com cuidado, uma vez que ele pode resultar em loops infinitos se não for controlado adequadamente. É fundamental ter uma condição que eventualmente seja satisfeita para que o loop possa ser encerrado.

Esse é um exemplo da versatilidade do loop `while` com `break` em Python, permitindo que você crie estruturas de repetição personalizadas para atender a diferentes necessidades de programação.

---
