from random import choice

n1 = input('Qual o primeiro nome? ')
n2 = input('Qual o segundo nome? ')
n3 = input('Qual o terceiro nome? ')
n4 = input('Qual o quarto nome? ')

print('O nome escolhido foi: {}.'.format(choice([n1, n2, n3, n4])))