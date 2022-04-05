#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while

termo = int(input('Qual o primeiro termo da PA? '))
ntermo = int(input('Até que termo você quer saber? '))
razao = int(input('Qual a razão da PA? '))
npa = termo + (ntermo) * razao
while termo != npa:
    print(f'{termo} → ', end='')
    termo += razao
print('FIM')




