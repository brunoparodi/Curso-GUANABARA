preco = float(input('Informe o preço do produto: R$'))
desconto = preco * (5 / 100)
print('O preço com desconto é: R${:.2f}.'.format(preco - desconto))
