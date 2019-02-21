salario = float(input('Qual o salario do funcionário? R$'))
aumento = salario * (15 / 100)
print('O aumento é de R$ {:.2f} e o novo salário é de R${:.2f}.'.format(aumento, salario + aumento))