#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1 , num+1 ):
    if num % c == 0:
        print(f'\33[32m{c}\33[m ', end=' ')
        tot+=1
    else:
        print(f'\33[31m{c}\33[m', end=' ')

print(f'\nO número {num} foi divisível {tot} vezes!')
if tot  == 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele NãO é primo!')
