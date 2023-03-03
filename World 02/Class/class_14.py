"""for i in range(1, 10):
    print(i)
print('The end.')
"""
"""c = 0
while c < 10:
    c += 1
    print(c)
print('The end.')
"""
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
