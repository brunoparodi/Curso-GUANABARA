vel = int(input('Qual a velocidade do carro? '))
print('' if vel <= 80 else 'Foi multado em R$ {}.'.format((vel - 80) * 7))

