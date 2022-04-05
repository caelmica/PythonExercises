#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
r = 'S'
while r == 'S':
    print('''SUAS OPÇÕES:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    jogador = int(input('O que você escolhe? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print('-='*20)
    print(f'O computador jogou: {itens[computador]} ')
    print(f'Você jogou: {itens[jogador]}')
    print('-='*20)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VOCÊ GANHOU!')
        elif jogador == 2:
            print('VOCÊ PERDEU!')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1:
        if jogador == 0:
            print('VOCÊ PERDEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('VOCÊ GANHOU!')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2:
        if jogador == 0:
            print('VOCÊ GANHOU!')
        elif jogador == 1:
            print('VOCÊ PERDEU!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('JOGADA INVÁLIDA!')
    r = str(input('Quer continuar? [S/N]: ').upper())
print('FIM!')
