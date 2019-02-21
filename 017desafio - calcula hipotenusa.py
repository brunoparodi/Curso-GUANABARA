from math import hypot

c1 = float(input('Informe o cateto 1: '))
c2 = float(input('Informe o cateto 2: '))
print('A hipotenusa de {} e {} é: {:.2f}.'.format(c1, c2, hypot(c1, c2)))

