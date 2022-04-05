#Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]
for n in range (1,8):
    num = int(input(f'Digite o {n}o número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Números pares: {sorted(numeros[0])}')
print(f'Números impares: {sorted(numeros[1])}')