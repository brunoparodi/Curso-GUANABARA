# from random import randrange
# num_pc = randrange(0, 5, 1)
# num_user = int(input('De 0 a 5, qual número você acha que o PC escolheu? '))
# if num_user == num_pc:
#     print('Parabéns, você acertou!!!')
# else:
#     print('Você errou!! O PC escolheu {}.'.format(num_pc))

from random import randint
from time import sleep
computador = randint(0, 5)
print('= # ' * 20)
print('Estou pensando em um número...')
print('= # ' * 20)
sleep(3)
jogador = int(input('Pronto, já escolhi. Qual número acha que foi? '))

if computador == jogador:
    print('Droga, perdi. PARABÉNS, você acertou.')
else:
    print(f'HA HA HA, ganhei!!! Eu escolhi o número {computador}')