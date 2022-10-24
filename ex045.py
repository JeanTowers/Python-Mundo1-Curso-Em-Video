# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Tente me vencer, escolhe sua opção')
print('[0] PEDRA \n[1] PAPEL \n[2] TESOURA')

jogador = int(input('Qual sua jogada? '))

print('JO')
sleep(1)
print('KEN') 
sleep(1)
print('PO!!!')
sleep(1)
print('=' * 27)
print(' Computador Escolheu {}'.format(itens[computador]))
print('  Jogador Escolheu {}'.format(itens[jogador]))
print('=' * 27)

if computador == 0: # PEDRA
    if jogador == 0:
        print('      Empate!!!')

    elif jogador == 1:
        print('      Você Ganhou!!!')

    elif jogador == 2:
        print('      Você Perdeu!!!')

elif computador == 1: # PAPEL
    if jogador == 0:
        print('      Você Perdeu!!!')

    elif jogador == 1:
        print('      Empate!!!')

    elif jogador == 2:
        print('      Você Ganhou!!!')

elif computador == 2: # TESOURA
    if jogador == 0:
        print('      Você Ganhou!!!')

    elif jogador == 1:
        print('      Você Perdeu!!!')

    elif jogador == 2:
        print('      Empate!!!')
