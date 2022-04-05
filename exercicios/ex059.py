#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

sair = False
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
from time import sleep

while opcao != 5:
    print('''ESCOLHA A OPÇÃO QUE QUER REALIZAR:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('OPÇÃO ESCOLHIDA: '))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}!')
        opcao = 5
    elif opcao == 2:
        print(f'{n1} multiplicado por {n2} é {n1*n2}!')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}!')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        sair = True
    else:
        print('Opção inválida!')
    print('CARREGANDO MENU NOVAMENTE...')
    sleep(3)
print('FIM')