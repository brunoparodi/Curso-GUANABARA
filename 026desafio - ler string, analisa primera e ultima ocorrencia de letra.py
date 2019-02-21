frase = str(input('Digite uma frase: ')).strip().lower()

print('''
A letra A apareceu {} vezes na frase.
A primeira letra A apareceu na posição {}.
A última letra A apareceu na posição {}.
'''.format(
    frase.count('a'),
    frase.find('a') + 1,
    frase.rfind('a') + 1
))
