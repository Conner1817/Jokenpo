import random
import sys
import os
import string
from random import randint

playerpts = 0
cpupts = 0

cpu = 'Pedra', 'Papel', 'Tesoura'


def random_string(length=1):
    cpu = 'Pedra', 'Papel', 'Tesoura'
    return ''.join(random.choice(cpu) for i in range(length))


my_random = random_string(1)
random.choice(cpu)

print('\nPedra, Papel ou Tesoura.')

jogada = input('\nFaça sua jogada: ')

if jogada == 'Pedra' and my_random == 'Tesoura':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nVitória!')

elif jogada == 'Pedra' and my_random == 'Papel':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nDerrota!')

elif jogada == 'Pedra' and my_random == 'Pedra':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nEmpate!')

elif jogada == 'Papel' and my_random == 'Pedra':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nVitória!')

elif jogada == 'Papel' and my_random == 'Tesoura':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nDerrota!')

elif jogada == 'Papel' and my_random == 'Papel':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nEmpate!')

elif jogada == 'Tesoura' and my_random == 'Papel':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nVitória')

elif jogada == 'Tesoura' and my_random == 'Pedra':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nDerrota!')

elif jogada == 'Tesoura' and my_random == 'Tesoura':
        print('\nJOGADOR: {} X {} :CPU'.format(jogada, my_random))
        print('\nEmpate!')

else:
        print('OPÇÃO INVÁLIDA! Lembre-se: o nome do jogo é PEDRA, PAPEL ou TESOURA. '
              'São apenas 3 opções de escolha')