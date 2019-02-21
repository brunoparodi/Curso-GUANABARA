#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <= 3 else 'carro velho')

# nome = str(input('Qual é seu nome? '))
# if nome == 'Gustavo':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) /2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns')
else:
    print('Sua média foi ruim! Estude mais!!')

print('PARABÉNS!!' if m >=6 else 'ESTUDE MAIS!!')  # CONDIÇÕES SIMPLIFICADAS
