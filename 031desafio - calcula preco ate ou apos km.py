km = int(input('Quantos quilometros serão a viagem? '))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f'O preço da passagem é R${preco :.2f} reais.')