nome = str(input('Qual seu nome completo? ')).lower().strip()

print('Seu nome tem Silva? {}'.format(nome.find('silva') != -1))  # .format('silva' in nome)