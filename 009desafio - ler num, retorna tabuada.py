n = int(input('Informe um número inteiro: '))
for x in range(1, 11):
    print('{:2} x {} = {:2}'.format(x, n, x * n))