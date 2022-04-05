#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = somamil = maisbarato = cont = menor = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço desse produto: R$ '))
    maisbarato = preco
    maiscaro = preco
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        somamil += 1
    parar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while parar not in 'SN':
        parar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if parar == 'N':
        break
print(f'Compra finalizada. Total: R${total:.2f}')
print(f'Dos produtos comprados, {somamil} custam mais de R$1000.00!')
print(f' O produto mais barato é {barato}')

