number = int(input('Write a number: '))
factorial = 1

while(number > 0):
    factorial *= number
    number = number - 1
print(f'Factorial: {factorial}')
