"""
Programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar. Calcular o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou então o empréstimo será negado.

Program to approve the bank loan for the purchase of a house. The program 
will ask for the home's value, the buyer's salary and in how many years he will pay.
Calculate the amount of the monthly installment, knowing that it cannot exceed 30% 
of the salary or else the loan will be denied.
"""
value_of_house = float(input('What is the value of the house:R$'))
salary = float(input('What is your salary R$:'))
years = int(input('In how many years will you pay the house?'))
monthly_installment = value_of_house/(years*12)
minimum = salary * 30/100
print('Monthly installments will be R${:.2f}'.format(monthly_installment))
if monthly_installment <= minimum:
    print('Accepted loan 😀')
else:
    print('Denied loan ⚠')
