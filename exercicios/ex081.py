#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.                                                                                                                                               A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
cont = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    resp = 's'
    if resp not in 'SN':
        while True:
            resp = input('Quer continuar? [S/N] ').strip().upper()[0]
            if resp in 'SN':
                break
    if resp == 'N':
        break
print(f'Foram digitados {cont} números.')
print(f'Valores digitados: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
