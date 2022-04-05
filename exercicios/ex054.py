#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
contmaior = 0
contn = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if (atual - nasc) >= 21:
     contmaior += 1
    else:
        contn += 1
print(f'Das pessoas informadas {contmaior} são maiores de idade e {contn} ainda não são!')