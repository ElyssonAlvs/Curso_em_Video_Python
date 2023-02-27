"""
Programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- À vista dinheiro/cheque : 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3X ou mais no cartão : 20% juros

Program that calculates the amount to be paid for a product, considering its
Normal price and payment condition:
- Cash/check payment: 10% discount
- Cash on card: 5% discount
- In up to 2 installments on the card: normal price
- 3X or more on the card: 20% interest
"""
price_product = float(input('Write the price of product:'))
payment = int(input('''Choice the method payment:
1 - Cash/check pyment
2 - Cash on card
3 - In up to 2 installments on the card
4 - 3x or more on the card
-> '''))
if payment == 1:
    price_product = price_product - (price_product * 0.1)
    print('Price for pay: {:.2f}'.format(price_product))
elif payment == 2:
    price_product = price_product(price_product * 0.05)
elif payment == 3:
    installment = price_product / 2
    print('Price of procuct: {:.2f}'.format(price_product))
    print('Installments : {:.2f}'.format(installment))
elif payment == 4:
    installments = int(input('How munch installments:'))
    total = price_product + (price_product * 0.2)
    qtd_installments = total / installments
    print('Price of product: {:.2f}'.format(total))
    print('Installments: {:.2f}'.format(qtd_installments))
else:
    total = 0
    print('INVALID OPTION!')
    print(f'Price of product: {total}')
