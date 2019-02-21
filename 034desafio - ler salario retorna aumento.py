salario = float(input('Qual é seu salário: '))

if salario >= 1250.00:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print(f'Seu novo salário é de R${novo :.2f}.')