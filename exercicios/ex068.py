#Faça um programa que jogue par ou ímpar com o computador.
# jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
num = soma = placar = 0
print('-='*10)
print('JOGO DE PAR OU IMPAR')
print('-='*10)
while True:
    computador = randint (0,9)
    poi = input('O que você escolhe [PAR/IMPAR]? ').upper().strip()
    jogador = int(input('Que número até 9 você escolhe? '))
    soma = jogador + computador
    print(f'Você escolheu {poi}. O computador escolheu {computador} e você {jogador}.')
    if poi == 'PAR' and soma % 2 == 0:
        placar += 1
        print(f'{soma} é PAR, ganhou!')
    elif poi == 'IMPAR' and soma % 2 == 1:
        placar += 1
        print(f'{soma} é IMPAR, ganhou!')
    else:
        break
print(f'{soma} não é {poi}. GAME OVER, o computador ganhou!')
print(f'Você ganhou {placar} vezes seguidas!')
