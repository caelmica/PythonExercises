#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta
from random import randint
lista = list()
sorteios = list()
print('*-'*30)
print(f'GERADOR DE JOGOS DA MEGASENA')
print('*-'*30)
jogos = int(input('Quantos jogos quer jogar? '))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    sorteios.append(lista[:])
    lista.clear()
    tot += 1
sorteios.sort()
print(sorteios)