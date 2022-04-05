#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = cont = maior = menor = media = soma = 0
lista = []
parar = False
while parar != True:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    media = soma/cont
    parar = input('Parar? [S/N] ').strip().upper()
    if parar == 'S':
            parar = True
    lista += [num]
print(f'A média dos valores digitádos é {media}.')
print(f'O maior valor digitado é {max(lista)} e o menor valor é {min(lista)}')