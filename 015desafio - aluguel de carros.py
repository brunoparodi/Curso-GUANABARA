dias_alugados = int(input('Quantos dias o carro foi locado? '))
km_rodados = float(input('Quantos km foi percorrido com o carro? '))

preco_km = 0.15
preco_dia = 60
total_km = km_rodados * preco_km
total_dia = dias_alugados * preco_dia
print('O valor  total do aluguel é de R$ {:.2f} referente a R$ {:.2f} pela km e R$ {:.2f} pelas diárias.'.format(total_dia + total_km, total_km, total_dia))
