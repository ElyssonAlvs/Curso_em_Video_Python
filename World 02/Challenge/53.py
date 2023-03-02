"""
Leia uma frase e diga se é palíndromo, desconsiderando os espaços

Read a sentence and say if it is a palindrome, disregarding the spaces
"""
phrase = str(input('Write a phrase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
rev_phrase = together[::-1]
if rev_phrase == together:
    print('Palindrome')
else:
    print('Is not palindrome')
