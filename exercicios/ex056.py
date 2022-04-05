#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
#No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
velho = 0
nomevelho = ''
contmu = 0
for p in range(1, 5):
    nome = str(input(f'Escreva o nome da {p}ª pessoa: ')).strip()
    idade = int(input(f'Escreva a idade da {p}ª pessoa: '))
    sexo = str(input(f'Escreva o sexo da {p}ª pessoa [M/F]: ')).strip()
    somaidade += idade
    media = somaidade/4
    if p == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmu += 1
print(f'A média de idade é {media:.0f} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {velho} anos!')
print(f'{contmu} mulheres tm menos de 20 anos de idade')