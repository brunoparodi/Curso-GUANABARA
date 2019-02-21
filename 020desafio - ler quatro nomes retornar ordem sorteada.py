from random import sample

n1 = input('Nome 01: ')
n2 = input('Nome 02: ')
n3 = input('Nome 03: ')
n4 = input('Nome 04: ')

print('A ordem sorteada foi: {}'.format(sample([n1, n2, n3, n4], 4)))

