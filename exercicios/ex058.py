#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
titulo = ' JOGO DA ADIVINHAÇÃO 2.0 '
computador = randint(0, 10)
palpites = 0
print('-='*25)
print(titulo.center(50, '*'))
print('-='*25)
print('Vou pensar num número, tente adivinhar qual....')
jogador = int(input('Em que número pensei? '))
while computador != jogador:
    jogador = int(input(('Não foi esse, chute outro! ')))
    palpites += 1
    if computador == jogador:
        print(f'Parabéns, eu pensei no número {computador}!')
print(f'Você acertou em {palpites+1} palpites!')
