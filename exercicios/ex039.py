# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

data = int(input('Em que ano você nasceu? '))
atual = int(input('Em que ano estamos? '))
alistar = data + 18
idade = atual - data
print(f'Seu ano de alistamento é {alistar}.')
if idade == 18:
    print(f'Você já está com {idade} anos, está na hora de se alistar, procure a junta mais próxima dá sua casa!')
elif idade > 18:
    print(f'Você tem {idade} anos.Você passou {atual-alistar} anos do prazo de alistamento!')
else:
    print(f'Você ainda não está na idade para se alistar! Faltam {abs(atual-alistar)} anos! ')
