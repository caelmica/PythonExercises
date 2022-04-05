#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaimpar = []
listapar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    elif num % 2 == 1:
        listaimpar.append(num)
    resp = 's'
    if resp not in 'SN':
        while True:
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()
            if resp in 'SN':
                break
    if resp == 'N':
        break
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {listapar}')
print(f'Os números impares digitados foram: {listaimpar}')