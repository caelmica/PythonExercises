#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.


cont18 = conthomem = contmulher = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo: [M/F] ').upper().strip()[0]
    if idade > 18:
        cont18 += 1
    if sexo in 'Mm':
        conthomem += 1
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
    parar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if parar == 'N':
        break
    elif parar not in 'SsNn':
        print('Opção inválida!')
        break
print(f'{cont18} pessoas tem mais de 18 anos.')
print(f'{conthomem} homens foram cadastrados.')
print(f'{contmulher} mulheres tem menos de 20 anos.')

