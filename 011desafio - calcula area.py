largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura * altura
tinta = 2
print('A area da parede é {} e você precisa de {} litros.'.format(area, (area // tinta) + 1))