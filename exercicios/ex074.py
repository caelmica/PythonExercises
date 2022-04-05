# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numero = (randint(0,100),randint(0,100),randint(0,100), randint(0,100), randint(0,100))
print(f'Os números gerados são: {numero}')
print(f'O maior valor gerado é {max(numero)}')
print(f'O menor valor gerado é {min(numero)}')