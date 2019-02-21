reta1 = float(input('Tamanho da reta 1: '))
reta2 = float(input('Tamanho da reta 2: '))
reta3 = float(input('Tamanho da reta 3: '))

if reta1 >= (reta2 + reta3) or reta2 >= (reta1 + reta3) or reta3 >= (reta1 + reta2):
    print('Não forma.')
else:
    print('Formam um triângulo.')
