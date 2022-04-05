#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = list()
pessoas = list()
peso = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp ='s'
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Opção inválida!')
        elif resp in 'SN':
            break
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {max(peso)} e o menor foi de {min(peso)}')