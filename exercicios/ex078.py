#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for n in range (1,6):
    num = int(input(f'Digite o {n}° número: '))
    lista.append(num)
print(f'O maior valor digitado foi {max(lista)} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i+1}, ', end='')
print(f'\nO menor valor digitado foi {min(lista)} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i + 1}, ', end='')
