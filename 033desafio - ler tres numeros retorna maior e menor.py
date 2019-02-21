num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

if num1 > num2 > num3:
    print(f'O maior número é {num1} e o menor número é {num3}.')
if num1 > num3 > num2:
    print(f'O maior número é {num1} e o menor número é {num2}.')
if num2 > num1 > num3:
    print(f'O maior número é {num2} e o menor número é {num3}.')
if num2 > num3 > num1:
    print(f'O maior número é {num2} e o menor número é {num1}.')
if num3 > num1 > num2:
    print(f'O maior número é {num3} e o menor número é {num2}.')
if num3 > num2 > num1:
    print(f'O maior número é {num3} e o menor número é {num1}.')
else:
    print('Os números são iguais.')