"""n = int(input('Write a number:'))
for c in range(0, n+1):
    print(c)
print('The end')
"""
s = int(input('Start: '))
e = int(input('End: '))
p = int(input('Pass: '))
for c in range(s, e+1, p):
    print(c)
print('The end')
