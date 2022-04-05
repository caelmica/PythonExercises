#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint(0,5)
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, eu realmente pensei no número {}!'.format(computador))
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')
