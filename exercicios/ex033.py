#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite um terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor é {menor}!')
print(f'O maior valor é {maior}!')


