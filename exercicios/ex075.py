#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

cont9 = 0

numeros = (int(input(f'Digite um número: ')), int(input(f'Digite um número: ')),
           int(input(f'Digite um número: ')), int(input(f'Digite um número: ')))
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado.')
print(f'Você digitou os números {numeros}.')
print('Os números pares digitados são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
