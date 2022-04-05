#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listanum = []
while True:
    num = (int(input('Digite um número: ')))
    if num not in listanum:
        listanum.append(num)
        print('Número adicionado à lista!')
    else:
        print('Número já existe na lista')
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
            break
print(f'Os números digitados foram {sorted(listanum)}')
