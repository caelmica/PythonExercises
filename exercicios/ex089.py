#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.

lista = list()

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    lista.append([nome, [nota1, nota2], media])
    resp = 's'
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('*'*30)
print(f'{"BOLETIM":^30}')
print('_'*30)
print(f'{"Nr":<4}{"NOME":<10}{"MÉDIA":>8}')
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.2f}')
while True:
    notas = int(input('Quer mostrar as notas de qual aluno? [999 interrompe] '))
    if notas == 999:
        break
    if notas < len(lista):
        print(f'As notas de {lista[notas][0]} são {lista[notas][1]}')
print('FIM!')