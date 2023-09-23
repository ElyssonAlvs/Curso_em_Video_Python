
# Condicionais em Python - Aula 12

Em Python, as condicionais são estruturas de controle de fluxo que permitem que um programa tome decisões com base em condições específicas. As condicionais mais comuns em Python são `if`, `elif` (abreviação de "else if") e `else`. Vamos analisar o código a seguir para entender como essas condicionais são usadas:

```python
name = str(input('What is your name ?'))
if name == 'Elysson':
    print('This is a beautiful name')
elif name == 'Peter' or name == 'Maria' or name == 'Paul':
    print('Your name is very famous in Brazil.')
elif name in 'Ana Elizabeth Rose Julie':
    print('This is beautiful female name')
print(f'Good Morning, {name}')
```

## `if`

- A estrutura `if` é usada para testar uma condição. No código acima, a condição testada é se `name` é igual a 'Elysson'.
- Se a condição for verdadeira, o bloco de código dentro do `if` é executado, e ele imprime "This is a beautiful name".
- Caso contrário, o programa avança para a próxima condicional.

## `elif` (else if)

- A estrutura `elif` permite adicionar condições adicionais que são testadas somente se as condições anteriores forem falsas.
- No código, se o nome não for 'Elysson', o programa verifica se o nome é igual a 'Peter', 'Maria' ou 'Paul'.
- Se alguma dessas condições for verdadeira, o bloco de código dentro do `elif` é executado, e ele imprime "Your name is very famous in Brazil."
- Se nenhuma das condições for verdadeira, o programa avança para a próxima condicional.

## `else`

- A estrutura `else` é usada para executar um bloco de código quando nenhuma das condições anteriores é verdadeira.
- No código acima, não há um bloco `else` explícito, mas o último `print(f'Good Morning, {name}')` será executado independentemente das condições anteriores. Portanto, "Good Morning" sempre será impresso no final.

## Conclusão

As condicionais em Python permitem que você crie lógica de decisão em seu código, permitindo que ele se comporte de maneira diferente com base em condições específicas. Você pode usar `if`, `elif` e `else` para lidar com várias possibilidades e cenários em seu programa. É importante lembrar que apenas um bloco de código dentro das condicionais é executado, dependendo da primeira condição verdadeira encontrada.