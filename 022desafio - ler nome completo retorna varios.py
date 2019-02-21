nome = str(input('Qual é seu nome completo? ')).strip()
print('''
Todas as letras maiúsculas: {}
Todas as letras minúsculas: {}
Seu nome completo (sem espaços) tem {} letras.
Seu primeiro nome {} tem {} letras.
'''.format(
    nome.upper(),
    nome.lower(),
    len(nome.replace(' ', '')),  # .format(len(nome) - nome.count(' '))
    nome.split()[0], len(nome.split()[0])  # .format(nome.find(' '))
))