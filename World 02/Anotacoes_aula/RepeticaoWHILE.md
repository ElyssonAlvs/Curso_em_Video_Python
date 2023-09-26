
# Estrutura de Repetição `while` em Python - Aula 14 e 15

A estrutura de repetição `while` em Python é utilizada quando você deseja repetir um bloco de código enquanto uma condição específica é verdadeira. Em outras palavras, o código dentro do bloco `while` é executado repetidamente até que a condição definida se torne falsa. Aqui está uma comparação entre a estrutura `for` e a estrutura `while` em Python:

### Estrutura `for`:
```python
for i in range(1, 10):
    print(i)
print('The end.')
```

Neste exemplo, o `for` é usado para iterar sobre uma sequência de números de 1 a 9 e imprimir cada número. O loop termina após a iteração de todos os valores na sequência.

### Estrutura `while`:
```python
c = 0
while c < 10:
    c += 1
    print(c)
print('The end.')
```

Aqui, usamos a estrutura `while`. O loop continuará enquanto a condição `c < 10` for verdadeira. No início, `c` é 0, e a cada iteração, incrementamos `c` em 1. O loop continuará até que `c` seja igual a 10, momento em que a condição se tornará falsa e o loop será encerrado. Em seguida, ele imprime "The end."

### Exemplo Adicional:

```python
# Zero for stop
n = 1
even = odd = 0
while n != 0:
    n = int(input('Write a value: '))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'Number of even: {even}')
print(f'Number of odd: {odd}')
```

Neste último exemplo, o programa solicita repetidamente ao usuário que insira um valor até que o valor inserido seja igual a zero. O loop `while` continua enquanto `n` não é igual a zero. Durante cada iteração, o programa verifica se o número inserido é par ou ímpar e mantém a contagem de números pares e ímpares. O loop é encerrado quando o usuário insere zero, e o programa imprime o número de valores pares e ímpares inseridos.

A estrutura de repetição `while` é uma ferramenta poderosa para criar loops em Python, especialmente quando você não sabe antecipadamente quantas vezes o loop precisará ser executado. Certifique-se sempre de ter uma condição que eventualmente se torne falsa para evitar loops infinitos.

